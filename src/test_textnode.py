import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_uneq_text(self):
        node = TextNode("This is a different text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.LINK, "link")
        node2 = TextNode("This is a text node", TextType.LINK, "link")
        self.assertEqual(node, node2)

    def test_uneq_link(self):
        node = TextNode("This is a text node", TextType.LINK, "diff link")
        node2 = TextNode("This is a text node", TextType.LINK, "link")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
