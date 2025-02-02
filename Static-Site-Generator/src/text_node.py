from typing import Optional, Union
from enum import Enum
from leaf_node import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

TAG_TYPE = {
    TextType.TEXT: None,  # no wrapping tag for plain text
    TextType.BOLD: "b",
    TextType.ITALIC: "i",
    TextType.CODE: "pre",
    TextType.LINK: "a",
    TextType.IMAGE: "img",
}

class TextNode():

    def __init__(self, text: str, text_type: TextType, props: Optional[Union[str, dict]] = None):
        '''
        Initializes a TextNode instance.

        Parameters:
            text (str): String of text.
            text_type (TextType): Defined enum value.
            props (Union[str, dict], optional): Optional string or dictionary attributes. Defaults to None.
        '''
        self.text = text
        self.text_type = text_type
        self.props = props

    # object string representation
    def __repr__(self):
        return f"TextNode(text=\"{self.text}\", text_type={self.text_type}, props={self.props})"

    # equals
    def __eq__(self, other):
        equality = False
        if isinstance(other, TextNode):
            equality = True if self.text == other.text and self.text_type == other.text_type and self.props == other.props else False
        return equality
    
    def to_leaf_node(self):
        special_value = [TextType.CODE, TextType.IMAGE]
        special_props = [TextType.TEXT, TextType.CODE, TextType.LINK, TextType.IMAGE]
        leaf_tag = TAG_TYPE.get(self.text_type, None)
        leaf_value = self.text if self.text_type not in special_value else (
            "" if self.text_type == TextType.IMAGE else
            f"<code class=\"language-{self.props.lower()}\">{self.text}</code>"
        )
        leaf_props = self.props if self.text_type not in special_props else (
            {"href":f"{self.props}"} if self.text_type == TextType.LINK else
            {"src":f"{self.props}", "alt": f"{self.text}"} if self.text_type == TextType.IMAGE else None
        )
        return LeafNode(leaf_tag, leaf_value, leaf_props)
