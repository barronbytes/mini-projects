from html_node import HTMLNode
from leaf_node import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        '''
        Initializes a ParentNode instance that extends HTMLNode.
        The `props` attribute is set to `None`.

        Parameters:
            tag (str): HTML tag.
            props (dict, optional): HTML attributes. Defaults to None.
            children (list): LeafNode list of children from parent tag.
        '''

        invalid_parameters = ", ".join([f"{param_name}=None" for param_name, param_value in zip(["tag", "children"], [tag, children]) if param_value is None])
        if invalid_parameters:
            raise ValueError(f"Invalid parameter(s): {invalid_parameters}")

        super().__init__(tag=tag, props=props, value=None, children=children)

    # override parent class
    def to_html(self):
        tag_props = self.props_to_html()
        tag_open = f"<{self.tag}{tag_props}>"
        tag_close = f"</{self.tag}>"

        return f"{tag_open}{tag_close}"
