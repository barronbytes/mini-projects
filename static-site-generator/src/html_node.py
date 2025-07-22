from typing import Optional


class HTMLNode():

    def __init__(self, tag: Optional[str] = None, props: Optional[dict] = None, 
             value: Optional[str] = None, children: Optional[list['HTMLNode']] = None):
        '''
        Initializes a HTMLNode instance.

        Parameters:
            tag (str, optional): HTML tag. Defaults to None.
            props (dict, optional): HTML attributes. Defaults to None.
            value (str, optional): HTML tag content. Defaults to None.
            children (list, optional): HTML tag children for parent tags. Defaults to None.
        '''
        self.tag = tag
        self.props = props
        self.value = value
        self.children = children

    # object string representation
    def __repr__(self) -> str:
        tag_display = f"\"{self.tag}\"" if self.tag is not None else None
        props_display = self.props if self.props is not None else None
        value_display = f"\"{self.value}\"" if self.value is not None else None
        children_display = self.children if self.children is not None else None
        return f"HTMLNode(tag={tag_display}, props={props_display}, value={value_display}, children={children_display})"

    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, HTMLNode):
            equality = True if self.tag == other.tag and self.props == other.props and self.value == other.value and self.children == other.children else False
        return equality

    def to_html(self):
        raise NotImplementedError("Not implemented.")
    
    def props_to_html(self) -> str:
        props_html= "".join(f' {k}="{v}"' for k, v in self.props.items()) if isinstance(self.props, dict) else ""
        return props_html
