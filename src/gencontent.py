import os
from markdown_blocks import BlockType, markdown_to_html_node

def extract_title(markdown):
    markdown_lines = markdown.split("\n")
    for line in markdown_lines:
        if line.startswith("# "):
            new_line = line[2:]
            return new_line.strip()
    raise Exception("no h1 header found")
    
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown_content = f.read()
    with open(template_path) as t:
        template_content = t.read()
    title = extract_title(markdown_content)
    html_node = markdown_to_html_node(markdown_content)
    html_string = html_node.to_html()

    page = template_content.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_string)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    dir_path = os.path.dirname(dest_path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath):
    if not os.path.exists(dir_path_public):
        os.mkdir(dir_path_public)

    content_items = os.listdir(dir_path_content)

    for item in content_items:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dir_path_public, item)

        if os.path.isfile(item_path):
            if item_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                generate_page(item_path, template_path, dest_path, basepath)

        else:
            generate_pages_recursive(item_path, template_path, dest_path, basepath)

   




