import unittest
from textnode import TextNode, TextType
from incline_markdown import split_nodes_delimiter,extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)

        result = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_code(self):
        node = TextNode("This is `code` text", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)