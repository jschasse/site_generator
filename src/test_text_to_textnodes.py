from textnode import *
from split_nodes_delimiter import *


def test_text_to_textnodes():
    input_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    expected_output = [
        TextNode("This is ", TextType.NORMAL),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.NORMAL),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.NORMAL),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.NORMAL),
        TextNode("link", TextType.LINK, "https://boot.dev"),
    ]

    result = text_to_textnodes(input_text)
    assert result == expected_output, f"Test failed: {result}"
    print("All tests passed!")

# Run the test
test_text_to_textnodes()