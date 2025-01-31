class HTMLNode():
    # string, dict, string, list
    def __init__(self, tag=None, props=None, value=None, children=None):
        self.tag= tag
        self.props= props
        self.value= value if children is None else None
        self.children= children if value is None else None

    # object string representation
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, props={self.props}, value={self.value}, children={self.children})"

    # equals
    def __eq__(self, other):
        equality = False
        if isinstance(other, HTMLNode):
            equality = True if self.tag == other.tag and self.props == other.props and self.value == other.value and self.children == other.children else False
        return equality

    def to_html(self):
        raise NotImplementedError("Not implemented.")
    
    def props_to_html(self):
        props_html= "".join(f' {k}="{v}"' for k, v in self.props.items()) if isinstance(self.props, dict) else ""
        return props_html
