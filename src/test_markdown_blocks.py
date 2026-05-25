import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

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