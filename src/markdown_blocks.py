def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    result = []
    for i in split_markdown:
       new_line = i.strip()
       if new_line == "":
           continue
       result.append(new_line)
    return result