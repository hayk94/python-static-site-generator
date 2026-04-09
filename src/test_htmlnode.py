import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_set_correctly(self):
        node = HTMLNode("a","hello", "Google link", {
	    "href": "https://www.google.com",
	    "target": "_blank",
	})
        self.assertEqual(node.props['href'],  "https://www.google.com")

    def test_tag_set_correctly(self):
        node = HTMLNode("a","hello", "Google link", {
	    "href": "https://www.google.com",
	    "target": "_blank",
	})
        self.assertEqual(node.tag,  "a")

    def test_props_to_html(self):
        node = HTMLNode("a","hello", "Google link", {
	    "href": "https://www.google.com",
	    "target": "_blank",
	})
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
