from textnode import TextNode
from textnode import TextType

def main():
    cat = TextNode("red" , TextType.LINK, "https://www.boot.dev")
    print(cat)
    
if __name__ == "__main__":
    main()