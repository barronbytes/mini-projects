import re
from typing import Optional

from enum import Enum
from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from inline_markdown import InlineMarkdown


class BlockType(Enum):
    H1 = ["h1", "_map_text_heading"]
    H2 = ["h2", "_map_text_heading"]
    H3 = ["h3", "_map_text_heading"]
    H4 = ["h4", "_map_text_heading"]
    H5 = ["h5", "_map_text_heading"]
    H6 = ["h6", "_map_text_heading"]
    PARAGRAPH = ["p", "_map_text_paragraph"]
    QUOTE = ["q", "_map_text_quote"]
    UL = ["ul", "_map_text_unordered_list"]
    OL = ["ol", "_map_text_ordered_list"]
    CODE = ["pre", "_map_text_code"]


BLOCK_DELIMITERS = {
    r"^\#{1}(?!\*)\s(?P<block_text>.*)": BlockType.H1,
    r"^\#{2}(?!\*)\s(?P<block_text>.*)": BlockType.H2,
    r"^\#{3}(?!\*)\s(?P<block_text>.*)": BlockType.H3,
    r"^\#{4}(?!\*)\s(?P<block_text>.*)": BlockType.H4,
    r"^\#{5}(?!\*)\s(?P<block_text>.*)": BlockType.H5,
    r"^\#{6}(?!\*)\s(?P<block_text>.*)": BlockType.H6,
    r"^\>(?!\>)\s(?P<block_text>.*)": BlockType.QUOTE,
    r"^\*{1}(?!\*)\s(?P<block_text>.*)": BlockType.UL,
    r"^\-{1}(?!\-)\s(?P<block_text>.*)": BlockType.UL,
    r"^\d+\.\s(?P<block_text>.*)": BlockType.OL,
    r"^\s*`{3}(?P<block_text>[\s\S]*?)`{3}\s*$": BlockType.CODE,
    r"^\s*`{1}(?P<block_text>[\s\S]*?)`{1}\s*$": BlockType.CODE,
}


class BlockMarkdown():

    def __init__(self, text: str):
        '''
        Initializes an BlockMarkdown instance.

        Parameters:
            text (str): String of text.
        '''
        self.md_text = text
        self.md_anchor = "div"

    # object string representation
    def __repr__(self) -> str:
        return f"BlockMarkdown(text=\"{self.md_text}\")"
    
    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, BlockMarkdown):
            equality = True if self.md_text == other.text else False
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
        matches = list(pattern.findall(self.md_text))
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
        all_indices = [i for i in range(min_max[0], min_max[1]+1)]
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

    @staticmethod
    def block_type(text: str) -> BlockType:
        match_result = BlockType.PARAGRAPH # default setting
        for delim, block_type in BLOCK_DELIMITERS.items():
            regex = delim
            pattern = re.compile(pattern=regex, flags=re.DOTALL | re.MULTILINE)
            found = re.match(pattern=pattern, string=text)
            if found and block_type not in [BlockType.QUOTE, BlockType.UL, BlockType.OL]:
                match_result = block_type
                break
            elif found and block_type in [BlockType.QUOTE, BlockType.UL, BlockType.OL]:
                splits = text.split("\n")
                found_items = [re.match(pattern=pattern, string=item) for item in splits]
                is_match = all(found_items)
                match_result = block_type if is_match else BlockType.PARAGRAPH
                break
        return match_result

    @staticmethod    
    def create_leaf_nodes(blocks: list[str], types: list[BlockType]) -> list[LeafNode]:
        maps = [getattr(BlockMarkdown, t.value[1]) for t in types] # convert block type string values to actual function references
        block_text = [map_func(text) for map_func, text in zip(maps, blocks)]
        inline_md = [InlineMarkdown(text) for text in block_text]
        text_nodes = [md.to_text_nodes() for md in inline_md]
        #leaf_nodes = [node.to_leaf_node() for nodes in text_nodes for node in nodes]
        #html = [node.to_html() for node in leaf_nodes]
        return len(text_nodes)

    @staticmethod
    def _map_text_paragraph(text: str) -> list[str]:
        return text.replace("\n", " ")

    def to_html_nodes(self):
        blocks = self.create_blocks()
        types = [BlockMarkdown.block_type(b) for b in blocks]
        leaves = BlockMarkdown.create_leaf_nodes(blocks, types)
        return leaves
