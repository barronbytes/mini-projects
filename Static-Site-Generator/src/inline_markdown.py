import re

from text_node import TextNode, TextType


DELIMITERS = {
    r"\*\*": TextType.BOLD,
    r"\_\_": TextType.BOLD,
    r"\*": TextType.ITALIC,
    r"\_": TextType.ITALIC,
    r"\`\`\`": TextType.CODE,
    r"\`": TextType.CODE,
    #"[]()": TextType.LINK,
    #"![]()": TextType.IMAGE,
}

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

    def get_markup_matches(self) -> list[tuple[int, int, str, TextType]]:
        results = []
        for delimter, node_type in DELIMITERS.items():
            regex = fr"{delimter}(?P<node_text>.*?){delimter}"
            pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
            matches = pattern.finditer(self.text)
            results.extend(
                (found.start(), found.end(), found.group("node_text"), node_type)
                for found in matches
                if found.group("node_text") != ""
            )
        return results
    
    def get_indices(self, markup_nodes: list[tuple[int, int, str, TextType]]) -> list[tuple[int, int]]:
        results = []
        results.append((0, markup_nodes[0][0]))
        results.extend(
            (markup_nodes[i-1][1], markup_nodes[i][0])
            for i in range(1, len(markup_nodes))
        )
        results.append((markup_nodes[-1][1], len(self.text)))
        return results
    
    def get_default_matches(self, indices: list[tuple[int, int]]) -> list[tuple[int, int, str, TextType]]:
        results = [
            (pair[0], pair[1], self.text[pair[0]:pair[1]], TextType.TEXT)
            for pair in indices
        ]
        return results

    def to_text_nodes(self):
        markup_nodes = self.get_markup_matches()
        markup_nodes.sort(key=lambda x: x[0])
        indices = self.get_indices(markup_nodes)
        default_nodes = self.get_default_matches(indices)
        all_nodes = sorted(markup_nodes+default_nodes, key=lambda x: x[0])
        return (
            [
                TextNode(node[2], node[3])
                for node in all_nodes
            ]
        )
