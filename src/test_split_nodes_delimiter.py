import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestHelpers(unittest.TestCase):
	def test_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

		self.assertListEqual(new_nodes, [
			TextNode("This is text with a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" word", TextType.TEXT),
		])
	# TODO: Write rest of tests
	# def test_bold(self):
	# 	node = TextNode("This is a text node", TextType.BOLD)
	# 	html_node = text_node_to_html_node(node)
	# 	self.assertEqual(html_node.tag, "b")
	# 	self.assertEqual(html_node.value, "This is a text node")
	#
	# def test_link(self):
	# 	node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
	# 	html_node = text_node_to_html_node(node)
	# 	self.assertEqual(html_node.tag, "a")
	# 	self.assertEqual(html_node.value, "This is a text node")
	# 	self.assertEqual(html_node.props["href"], "https://www.google.com")
	#
	# def test_img(self):
	# 	node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
	# 	html_node = text_node_to_html_node(node)
	# 	self.assertEqual(html_node.tag, "img")
	# 	self.assertEqual(html_node.props["alt"], "This is a text node")
	# 	self.assertEqual(html_node.props["src"], "https://www.google.com")

if __name__ == "__main__":
    unittest.main()
