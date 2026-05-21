from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Invalid Markdown syntax.")
        
        for i, piece in enumerate(split_node):
            if piece == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(piece, TextType.TEXT))
            else:
                new_nodes.append(TextNode(piece, text_type))

    return new_nodes