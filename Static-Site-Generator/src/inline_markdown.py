from typing import Optional
from text_node import TextNode, TextType


REGEX_FOR_DELIMETER_TYPE = {
    "**": TextType.BOLD,
    "__": TextType.BOLD,
    "*": TextType.ITALIC,
    "_": TextType.ITALIC,
    "```": TextType.CODE,
    "`": TextType.CODE,
    "[]()": TextType.LINK,
    "![]()": TextType.LINK,
}

class InlineMarkdown():
    pass
