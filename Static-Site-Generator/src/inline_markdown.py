import re

from text_node import TextNode, TextType


DELIMITERS = {
    r"\*\*": TextType.BOLD,
    r"\_\_": TextType.BOLD,
    r"\*": TextType.ITALIC,
    r"\_": TextType.ITALIC,
    r"\`\`\`": TextType.CODE,
    r"\`": TextType.CODE,
    r"\[(?P<link_text>.*?)\]\((?P<link_url>.*?)\)": TextType.LINK,
    r"\!\[(?P<image_text>.*?)\]\((?P<image_url>.*?)\)": TextType.IMAGE,
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
        if isinstance(other, TextNode):
            equality = True if self.text == other.text else False
        return equality

    def get_markup_matches(self) -> list[tuple[int, int, TextNode]]:
        results = []
        for delimiter, node_type in DELIMITERS.items():
            if node_type in [TextType.LINK, TextType.IMAGE]:
                regex = delimiter
            else:
                regex = fr"{delimiter}(?P<node_text>.*?){delimiter}"
            
            pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
            matches = pattern.finditer(self.text)

            for found in matches:
                if node_type == TextType.LINK:
                    results.append(self.map_for_link(found))
                elif node_type == TextType.IMAGE:
                    results.append(self.map_for_image(found))
                else:
                    node_text = found.group("node_text")
                    if node_text != "":
                        results.append(
                            self.map_for_code(found) if node_type == TextType.CODE else
                            (found.start(), found.end(), TextNode(node_text, node_type, None))
                        )
        return results
    
    def map_for_code(self, found: re.Match[str]) -> tuple[int, int, TextNode]:
        node_text = found.group("node_text")
        language = next(
            (lang for lang in CODE_LANGUAGES if node_text.lower().startswith(lang+" ")),
            ""
        )
        node_text = node_text[len(language):].lstrip()
        return (found.start(), found.end(), TextNode(node_text, TextType.CODE, language))
    
    def map_for_link(self, found: re.Match[str]) -> tuple[int, int, TextNode]:
        link_text = found.group("link_text")
        link_url = found.group("link_url")
        return (found.start(), found.end(), TextNode(link_text, TextType.LINK, link_url))

    def map_for_image(self, found: re.Match[str]) -> tuple[int, int, TextNode]:
        image_text = found.group("image_text")
        image_url = found.group("image_url")
        return (found.start(), found.end(), TextNode(image_text, TextType.IMAGE, image_url))

    def get_indices(self, markup_nodes: list[tuple[int, int, TextNode]]) -> list[tuple[int, int]]:
        results = []
        results.append((0, markup_nodes[0][0]))
        results.extend(
            (markup_nodes[i-1][1], markup_nodes[i][0])
            for i in range(1, len(markup_nodes))
        )
        results.append((markup_nodes[-1][1], len(self.text)))
        return results
    
    def get_default_matches(self, indices: list[tuple[int, int]]) -> list[tuple[int, int, TextNode]]:
        results = [
            (pair[0], pair[1], TextNode(self.text[pair[0]:pair[1]], TextType.TEXT, None))
            for pair in indices
        ]
        return results

    def to_text_nodes(self) -> list[TextNode]:
        markup_nodes = self.get_markup_matches()
        markup_nodes.sort(key=lambda x: x[0])
        indices = self.get_indices(markup_nodes)
        default_nodes = self.get_default_matches(indices)
        all_nodes = sorted(markup_nodes+default_nodes, key=lambda x: x[0])
        return ([node[2] for node in all_nodes])
