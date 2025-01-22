class HTMLNode():
    
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode: tag:{self.tag}, value:{self.value}, props{self.props}, children:{self.children}"