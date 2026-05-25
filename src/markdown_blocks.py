from enum import Enum
import re

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
