import re
from typing import Optional

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
        min_max, span = self._find_indices(matches)
        overlap = self._find_overlap(span)
        blocks = self._join_blocks(matches, min_max, overlap)
        return blocks

    def _create_patterns(self) -> list[str]:
        regex = r"^\s*(.*?)\s*$|\n+"
        pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
        matches = list(pattern.findall(self.text))
        return [m if m != "" else "\n" for m in matches]
    
    def _find_indices(self, matches: list[str]) -> tuple[list[int], Optional[list[tuple[int, int]]]]:
        is_single_list = 1 == len(matches)
        min_max = [0, 0] if is_single_list else [0, len(matches)-1]
        line_breaks = [i for i in range(len(matches)) if matches[i] == "\n"] if "\n" in matches else None
        span = [(i-1, i+1) for i in line_breaks] if (not is_single_list) and (line_breaks is not None) else None
        return (min_max, span)

    def _find_overlap(self, span: list[tuple[int, int]] | None) -> list[tuple[int, int]] | None:
        return (
            [
                (span[i][0], span[i][1]) if (1 == len(span)) or (i+1 == len(span)) or (span[i][1] != span[i+1][0]) else 
                (span[i][0], span[i+1][1])
                for i in range(len(span)) 
                if i == 0 or span[i][0] != span[i-1][1]
            ] if span else None
        )

    def _join_blocks(self, 
                    matches: list[str],
                    min_max: list[int],
                    overlap: list[tuple[int, int]] | None) -> list[str]:
        all_indices = [i for i in range(len(matches))]
        overlap_indices = self._find_overlap_indices(overlap)
        sole_indices = [i for i in all_indices if i not in overlap_indices]
        sole_blocks = [(i, matches[i]) for i in sole_indices]
        all_blocks = self._add_overlap_indices(overlap, matches, sole_blocks) if overlap else sole_blocks
        sorted_blocks = sorted(all_blocks, key = lambda x: x[0])
        return [block[1] for block in sorted_blocks]

    def _find_overlap_indices(self, overlap: list[tuple[int, int]] | None) -> list[int] | None:
        indices = []
        indices.extend(
            n
            for j, k in overlap
            for n in range(j, k+1) 
        ) if overlap else None
        return indices
    
    def _add_overlap_indices(self,
                    overlap: list[tuple[int, int]], matches: list[str],
                    blocks: list[tuple[int, str]]) -> list[tuple[int, str]]:
        return blocks + [(j, "".join(matches[j:k+1])) for j, k in overlap]

    def to_blocks(self):
        blocks = self.create_blocks()
