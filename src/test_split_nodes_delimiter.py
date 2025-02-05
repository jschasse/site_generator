import unittest
from textnode import *
from split_nodes_delimiter import *

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![alt text](https://example.com/image.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with an image ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_no_image(self):
        node = TextNode("This is text without an image", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_link_no_link(self):
        node = TextNode("This is text without a link", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()