import re
import itertools

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UL = "unordered list",
    OL = "ordered list",


BLOCK_DELIMITERS = {
    r"1": BlockType.PARAGRAPH,
    r"2": BlockType.HEADING,
    r"3": BlockType.CODE,    
    r"4": BlockType.QUOTE,
    r"5": BlockType.UL,
    r"6": BlockType.OL,
}

class BlockMarkdown():

    def __init__(self, text: str):
        '''
        Initializes an BlockMarkdown instance.

        Parameters:
            text (str): String of text.
        '''
        self.text = text

    # object string representation
    def __repr__(self) -> str:
        return f"BlockMarkdown(text=\"{self.text}\")"
    
    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, BlockMarkdown):
            equality = True if self.text == other.text else False
        return equality

    def create_blocks(self):
        regex = r"^\s*(.*?)\s*$|\n+"
        pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
        matches = list(pattern.findall(self.text))
        matches = [m if m != "" else "\n" for m in matches]
        return matches

    def to_blocks(self):
        blocks = self.create_blocks()
