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

    def create_blocks(self) -> list[str]:
        matches = self._create_patterns()
        is_single_list = 1 == len(matches)
        i_min_max = [0] if is_single_list else [0, len(matches)-1]
        i_breakers = [i for i in range(len(matches)) if matches[i] == "\n"] if "\n" in matches else None
        i_spans = [(i-1, i+1) for i in i_breakers] if (not is_single_list) and (i_breakers is not None) else None

        i_spans_final = (
            [
                (i_spans[i][0], i_spans[i][1]) if (1 == len(i_spans)) or (i+1 == len(i_spans)) or (i_spans[i][1] != i_spans[i+1][0]) else 
                (i_spans[i][0], i_spans[i+1][1])
                for i in range(len(i_spans)) 
                if i == 0 or i_spans[i][0] != i_spans[i-1][1]
            ] if i_spans else None
        )
        return i_min_max, i_spans_final, matches

    def _create_patterns(self) -> list[str]:
        regex = r"^\s*(.*?)\s*$|\n+"
        pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
        matches = list(pattern.findall(self.text))
        return [m if m != "" else "\n" for m in matches]

    def to_blocks(self):
        blocks = self.create_blocks()
