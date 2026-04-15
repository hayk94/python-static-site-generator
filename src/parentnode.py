from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None):
		super().__init__(tag, None, children, props)
	
	def to_html(self):
		if self.children is None:
			raise ValueError("All parent nodes must have children.")
		if self.tag is None:
			raise ValueError("All parent nodes must have a tag.")
		tag = self.tag

		children_html = ""
		for child in self.children:
			children_html += child.to_html()	

		return f'<{tag}{self.props_to_html()}>{children_html}</{tag}>' 


	def __repr__(self):
		print(f"LeafNode tag: {self.tag} value: {self.value} props: {self.props}")
