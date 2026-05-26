from markdown_blocks import BlockType

def extract_title(markdown):
    markdown_lines = markdown.split("\n")
    for line in markdown_lines:
        if line.startswith("# "):
            new_line = line[2:]
            return new_line.strip()
    raise Exception("no h1 header found")
    