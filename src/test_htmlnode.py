from htmlnode import *

        
def main():
    data = {"href": "https://www.google.com"}
    data2 = {"href": "https://www.google.com", "target": "_blank"}
    data3 = {"fdsfgdsfg": "sdfsdgsdgsdg"}
    node = HTMLNode("p", "im goku", data2)
    node2 = HTMLNode("p", "im goku",  data)
    node3 = LeafNode("p", "This is a paragraph of text.")
    node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})  
    print(node.__repr__())
    print(node2.__repr__())
    print(node3.__repr__())
    print(node.props_to_html())
    print(node3.to_html())
    print(node4.to_html())


if __name__ == "__main__":
    main()