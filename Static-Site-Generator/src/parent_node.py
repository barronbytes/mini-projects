from html_node import HTMLNode


class ParentNode(HTMLNode):
    #def __init__(self, tag=None, props=None, value=None, children=None):
    def __init__(self, tag, children, props=None):
        '''
        Initializes a ParentNode instance that extends HTMLNode.
        The `children` attribute is set to `None`.

        Parameters:
            tag (str): HTML tag.
            props (dict, optional): HTML attributes. Defaults to None.
            children (list): HTML tag children for parent tags.
        '''

        invalid_parameters = ", ".join([f"{param_name}=None" for param_name, param_value in zip(["tag", "children"], [tag, children]) if param_value is None])
        if invalid_parameters:
            raise ValueError(f"Invalid parameter(s): {invalid_parameters}")

        super().__init__(tag=tag, props=props, value=None, children=children)
