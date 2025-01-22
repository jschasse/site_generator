from htmlnode import *

        
def main():
    data = {"href": "https://www.google.com"}
    data2 = {"href": "https://www.google.com", "target": "_blank"}
    data3 = {"fdsfgdsfg": "sdfsdgsdgsdg"}
    node = HTMLNode("p", "im goku", data2)
    node2 = HTMLNode("p", "im goku",  data)
    node3 = HTMLNode("p", "im goku",  data3)    
    print(node.__repr__())
    print(node2.__repr__())
    print(node3.__repr__())
    print(node.props_to_html())


if __name__ == "__main__":
    main()