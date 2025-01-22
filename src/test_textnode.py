import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://docs.python.org/3/reference/datamodel.html#object.__repr__")
        node2 = TextNode("This is a text node", TextType.NORMAL, "https://docs.python.org/3/reference/datamodel.html#object.__repr__")
        self.assertEqual(node, node2)

#if __name__ == "__main__":
#    unittest.main()