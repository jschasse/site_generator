import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: unmatched delimiter {delimiter}")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes



def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        original_text = node.text
        markdown_images = extract_markdown_images(original_text)
        
        if not markdown_images:
            new_nodes.append(node)
            continue
        
        for image_alt, image_url in markdown_images:
            sections = original_text.split(f"![{image_alt}]({image_url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            if len(sections) > 1:
                original_text = sections[1]
            else:
                original_text = ""
                
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
        

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        original_text = node.text
        markdown_links = extract_markdown_links(original_text)
        
        if not markdown_links:
            new_nodes.append(node)
            continue
        
        for link_alt, link_url in markdown_links:
            sections = original_text.split(f"[{link_alt}]({link_url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            if len(sections) > 1:
                original_text = sections[1]
            else:
                original_text = ""
                
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
        
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    return nodes