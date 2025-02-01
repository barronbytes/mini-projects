from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():

    def __init__(self, text, text_type, url=None):
        '''
        Initializes a TextNode instance.

        Parameters:
            text (str): String of text.
            text_type (TextType): Defined enum value.
            url (str, optional): Optional URL string. Defaults to None.
        '''
        self.text = text
        self.text_type = text_type
        self.url = url

    # object string representation
    def __repr__(self):
        url_display = f"\"{self.url}\"" if self.url is not None else None
        return f"TextNode(text=\"{self.text}\", text_type={self.text_type}, url={url_display})"

    # equals
    def __eq__(self, other):
        equality = False
        if isinstance(other, TextNode):
            equality = True if self.text == other.text and self.text_type == other.text_type and self.url == other.url else False
        return equality
