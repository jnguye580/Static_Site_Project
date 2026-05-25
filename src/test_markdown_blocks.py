import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph_block_to_block_type(self):
        block = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading_block_to_block_type(self):
        block = "###### This is a heading"
        expected = BlockType.HEADING
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_code_block_to_block_type(self):
        block = "```\nThis is a code type\n```"
        expected = BlockType.CODE
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_quote_block_to_block_type(self):
        block = """> This is a quote > This is still part of the same quote > Another quoted line"""
        expected = BlockType.QUOTE
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
        
    def test_unordered_list_block_to_block_type(self):
        block = """- This is a unordered_list - This is still part of the same unordered_list - Another unordered_list line"""
        expected = BlockType.UNORDERED_LIST
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_ordered_list_block_to_block_type(self):
        block = """1. This is a ordered_list 2. This is still part of the same ordered_list 3. Another ordered_list line"""
        expected = BlockType.ORDERED_LIST
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
 ```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = "##### This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>This is a heading</h5></div>"
        )
    
    def test_quote(self):
        md = """
> This is a quote
> This also a quote
> Still a quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote This also a quote Still a quote</blockquote></div>"
        )
    
    def test_unordered(self):
        md = """
- Apples
- Bananas
- Oranges
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Apples</li><li>Bananas</li><li>Oranges</li></ul></div>"
        )
    
    def test_ordered(self):
        md = """
1. Apples
2. Bananas
3. Oranges
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Apples</li><li>Bananas</li><li>Oranges</li></ol></div>"
        )