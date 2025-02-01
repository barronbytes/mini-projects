from html_node import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        '''
        Initializes a LeafNode instance that extends HTMLNode.
        The `children` attribute is set to `None`.

        Parameters:
            tag (str): HTML tag.
            props (dict, optional): HTML attributes. Defaults to None.
            value (str): HTML tag content.
        '''
        super().__init__(tag=tag, props=props, value=value, children=None)

    # override parent abstract class
    def to_html(self):
        tag_props = self.props_to_html()
        tag_open = f"<{self.tag}{tag_props}>" if self.tag is not None else ""
        tag_close = f"</{self.tag}>" if self.tag is not None else ""
        return f"{tag_open}{self.value}{tag_close}"
    