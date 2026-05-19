import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLnode(unittest.TestCase):
    def test_eq_to_html(self):
        node = HTMLNode
        with self.assertRaises(NotImplementedError):
            node.to_html(self)

    def test_eq_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })

        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_props_dict(self):
        node = HTMLNode(props={})

        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_one_prop(self):
        node = HTMLNode(props={
            "href": "https://www.google.com"
        })

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"'
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_props_leaf_to_html_p(self):
        node = LeafNode("a", "This is a paragraph of text.", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a paragraph of text.</a>')

    def test_none_tag_leaf_to_html_p(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_none_value_leaf_to_html_p(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
