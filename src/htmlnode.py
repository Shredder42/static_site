class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props:
            html = ''
            for k, v in self.props.items():
                html += f' {k}="{v}"'
            return html
        else:
            return ''

    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}; Value: {self.value}; Children: {self.children}; Props: {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise ValueError("Must have value")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"