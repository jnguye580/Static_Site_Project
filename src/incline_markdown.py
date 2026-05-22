import re
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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        current_text = node.text


        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"
            split_node = current_text.split(image_markdown, 1)

            if len(split_node) != 2:
                raise Exception("Invalid markdown image syntax")

            before_image = split_node[0]
            after_image = split_node[1]

            if before_image != "":
                new_nodes.append(TextNode(before_image, TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGES, image_url))

            current_text = after_image

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_links(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        current_text = node.text


        for image_alt, image_url in images:
            image_markdown = f"[{image_alt}]({image_url})"
            split_node = current_text.split(image_markdown, 1)

            if len(split_node) != 2:
                raise Exception("Invalid markdown image syntax")

            before_image = split_node[0]
            after_image = split_node[1]

            if before_image != "":
                new_nodes.append(TextNode(before_image, TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.LINK, image_url))

            current_text = after_image

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold_split = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    italic_split = split_nodes_delimiter(bold_split, "_", TextType.ITALIC_TEXT)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE_TEXT)
    images_split = split_nodes_image(code_split)
    link_split = split_nodes_link(images_split)
    return link_split