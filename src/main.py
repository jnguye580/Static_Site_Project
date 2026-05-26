from gencontent import generate_page, generate_pages_recursive
from textnode import TextNode, TextType
from copystatic import copy_static

def main():
    copy_static("static", "public")
    generate_pages_recursive("content/", "template.html", "public/")

    
if __name__ == "__main__":
    main()