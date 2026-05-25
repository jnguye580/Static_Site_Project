from enum import Enum
import re
from htmlnode import HTMLNode, ParentNode
from incline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    result = []
    for i in split_markdown:
       new_line = i.strip()
       if new_line == "":
           continue
       result.append(new_line)
    return result
    
def block_to_block_type(markdown_block):
    if re.match(r"^#{1,6} .+", markdown_block):
        return BlockType.HEADING

    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE

    lines = markdown_block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(re.match(r"^- .+", line) for line in lines):
        return BlockType.UNORDERED_LIST

    if all(
        re.match(rf"^{i}\. .+", line)
        for i, line in enumerate(lines, start=1)
    ):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        Node = block_to_html_node(block)
        children.append(Node)
    return ParentNode("div", children)
    
    
def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        text = " ".join(block.split("\n"))
        children = text_to_children(text)
        return ParentNode("p", children)
    
    elif block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        text = block.lstrip("#")
        new_block = text.strip()
        children = text_to_children(new_block)
        return ParentNode(f"h{level}", children)
    
    elif block_type == BlockType.CODE:
        code_text = block[3:-3].lstrip("\n")
        text_node = TextNode(code_text, TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        return ParentNode("pre", [
            ParentNode("code", [html_node])
        ])
    
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")

        cleaned_lines = []
        for line in lines:
            cleaned_line = line[1:].strip()
            cleaned_lines.append(cleaned_line)

        raw_text = " ".join(cleaned_lines)

        children = text_to_children(raw_text)
        return ParentNode("blockquote", children)
    
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")

        cleaned_lines = []
        for line in lines:
            cleaned_line = line[2:]
            item_children = text_to_children(cleaned_line)
            cleaned_lines.append(ParentNode("li",item_children))
        return ParentNode("ul", cleaned_lines)
    
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")

        cleaned_lines = []
        for line in lines:
            cleaned_line = line.split(". ", 1)[1]
            item_children = text_to_children(cleaned_line)
            cleaned_lines.append(ParentNode("li", item_children))
        return ParentNode("ol", cleaned_lines,)
        

def text_to_children(block):
    result = []
    text_nodes = text_to_textnodes(block)
    for nodes in text_nodes:
        result.append(text_node_to_html_node(nodes))
    return result