from textnode import *
from text_to_html import *
from split_nodes_delimiter import *

def main():
    test = TextNode("hello wanderer", TextType.BOLD, "https://www.boot.dev")
    print(test.__repr__())
    node3 = TextNode("lol", TextType.NORMAL)
    node3 = text_node_to_html_node(node3)
    print(node3.to_html())
    node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    sections = extract_markdown_links(node)
    image_alt = sections[0][0]
    image_link = sections[0][1]
    print(node.split(f"[{image_alt}]({image_link})"))





if __name__ == "__main__":
    main()