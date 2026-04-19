from textnode import TextType, TextNode
from leafnode import LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type is not TextType.TEXT:
			new_nodes.append(node)
		elif delimiter in node.text is False:
			raise Exception("Delimiter not found, invalid Markdown syntax")
		else:
			splitted_text = node.text.split(delimiter)
			for i in range(0, len(splitted_text)):
				text = splitted_text[i]
				if i == 1:
					new_nodes.append(TextNode(text, text_type))
				else:
					new_nodes.append(TextNode(text, TextType.TEXT))

	return new_nodes

