import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_2_children(self):
        child_node = LeafNode("span", "hello")
        child_node2 = LeafNode("b", "world")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>hello</span><b>world</b></div>"
        )
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_child(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_text_leaf_child(self):
        child_node = LeafNode(None, "hello")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>hello</div>")