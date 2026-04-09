from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, None, props)
	
	def to_html(self):
		if self.value is None:
			raise ValueError("All leaf nodes must have a value")
		if self.tag is None:
			return f"{value}"
		tag = self.tag
		value = self.value	
		return f'<{tag}{self.props_to_html()}>{value}</{tag}>' 


	def __repr__(self):
		print(f"LeafNode tag: {self.tag} value: {self.value} props: {self.props}")
