import re

from typing import Iterator
from text_node import TextNode, TextType


INLINE_DELIMITERS = {
    r"\*\*": TextType.BOLD,
    r"\_\_": TextType.BOLD,
    r"\*": TextType.ITALIC,
    r"\_": TextType.ITALIC,
    r"\`\`\`": TextType.CODE,
    r"\`": TextType.CODE,
    r"(?<!\!)\[(?P<link_text>.*?)\]\((?P<link_url>.*?)\)": TextType.LINK, # Link Regex: [text](url), ignores preceding !
    r"\!\[(?P<image_text>.*?)\]\((?P<image_url>.*?)\)": TextType.IMAGE, # Image Regex: ![text](url)
}

CODE_LANGUAGES = [
    "html", "css", "javascript",
    "python", "java",
]


class InlineMarkdown():

    def __init__(self, text: str):
        '''
        Initializes an InlineMarkdown instance.

        Parameters:
            text (str): String of text.
        '''
        self.text = text

    # object string representation
    def __repr__(self) -> str:
        return f"InlineMarkdown(text=\"{self.text}\")"

    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, InlineMarkdown):
            equality = True if self.text == other.text else False
        return equality
    
    def find_matches(self) -> list[tuple[list[re.Match[str]], TextType]]:
        matches = [
            (self._create_patterns(delim, node_type), node_type)
            for delim, node_type in INLINE_DELIMITERS.items()
        ]
        matches_found = any(m[0] for m in matches)
        return [] if not matches_found else matches

    def _create_patterns(self, delim: str, node_type: TextType) -> list[re.Match[str]]:
        regex = (
            delim if node_type in [TextType.LINK, TextType.IMAGE] else
            fr"{delim}(?P<node_text>.*?){delim}"
        )
        pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
        matches = list(pattern.finditer(self.text)) # return fresh list of matches instead of an exhausted iterator
        return matches

    def create_group_nodes(self, matches: list[tuple[list[re.Match[str]], TextType]]) -> list[tuple[int, int, TextNode]]:
        group_nodes = []
        for match_list, node_type in matches:
            group_nodes.extend(
                self._map_for_image(m) if node_type == TextType.IMAGE else 
                self._map_for_link(m) if node_type == TextType.LINK else
                self._map_for_code(m) if node_type == TextType.CODE else
                self._map_for_bold_italic(m, node_type)
                for m in match_list
            )
        return self._delete_group_nodes(group_nodes)

    def _map_for_image(self, m: re.Match[str]) -> tuple[int, int, TextNode]:
        image_text = m.group("image_text")
        image_url = m.group("image_url")
        return (m.start(), m.end(), TextNode(image_text, TextType.IMAGE, image_url))

    def _map_for_link(self, m: re.Match[str]) -> tuple[int, int, TextNode]:
        link_text = m.group("link_text")
        link_url = m.group("link_url")
        return (m.start(), m.end(), TextNode(link_text, TextType.LINK, link_url))
    
    def _map_for_code(self, m: re.Match[str]) -> tuple[int, int, TextNode]:
        node_text = m.group("node_text")
        language = next(
            (lang for lang in CODE_LANGUAGES if node_text.lower().startswith(lang+" ")),
            ""
        )
        node_text = node_text[len(language):].lstrip()
        return (m.start(), m.end(), TextNode(node_text, TextType.CODE, language))

    def _map_for_bold_italic(self, m: re.Match[str], node_type: TextType) -> tuple[int, int, TextNode]:
        node_text = m.group("node_text")
        return (m.start(), m.end(), TextNode(node_text, node_type, None))
    
    def _delete_group_nodes(self, group_nodes: list[tuple[int, int, TextNode]]) -> list[tuple[int, int, TextNode]]:
        return [
            node
            for node in group_nodes
            if not (node[2].text == "" and node[2].text_type in [TextType.BOLD, TextType.ITALIC])
        ]

    def get_indices(self, group_nodes: list[tuple[int, int, TextNode]]) -> list[tuple[int, int]]:
        indices = []
        indices.append((0, group_nodes[0][0]))
        indices.extend(
            (group_nodes[i-1][1], group_nodes[i][0])
            for i in range(1, len(group_nodes))
        )
        indices.append((group_nodes[-1][1], len(self.text)))
        return indices
    
    def create_default_nodes(self, indices: list[tuple[int, int]]) -> list[tuple[int, int, TextNode]]:
        default_nodes = [
            (pair[0], pair[1], TextNode(self.text[pair[0]:pair[1]], TextType.TEXT, None))
            for pair in indices
        ]
        return self._delete_default_nodes(default_nodes)
    
    def _delete_default_nodes(self, default_nodes: list[tuple[int, int, TextNode]]) -> list[tuple[int, int, TextNode]]:
        return [
            node
            for node in default_nodes
            if not (node[2].text == "" and node[2].text_type == TextType.TEXT)
        ]

    def to_text_nodes(self) -> list[TextNode]:
        matches = self.find_matches()
        all_nodes = []
        if matches:
            group_nodes = self.create_group_nodes(matches)
            group_nodes.sort(key=lambda x: x[0])
            indices = self.get_indices(group_nodes)
            default_nodes = self.create_default_nodes(indices)
            all_nodes = sorted(group_nodes + default_nodes, key=lambda x: x[0])
        else:
            all_nodes.append(TextNode(self.text, TextType.TEXT))
        return ([node[2] for node in all_nodes] if matches else all_nodes)
