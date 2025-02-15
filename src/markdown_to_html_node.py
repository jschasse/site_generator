from htmlnode import *
from split_nodes_delimiter import *
from markdown_to_blocks import *
from textnode import *

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children



def markdown_to_html_node(markdown):
    children = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            children.append(block_heading(block))
        if block_type == "unordered_list":
            children.append(block_list(block))
        if block_type == "ordered_list":
            children.append(olist_to_html_node(block))
        if block_type == "code":
            children.append(block_code(block))
        if block_type == "quote":
            children.append(block_quote(block))
        if block_type == "paragraph":
            children.append(block_paragraph(block))
        
    return ParentNode("div", children)
        
            
def block_heading(block):
    if block.startswith("#"):
        return LeafNode("h1", block.strip("# "))
    if block.startswith("##"):
        return LeafNode("h2", block.strip("## "))
    if block.startswith("###"):
        return LeafNode("h3", block.strip("### "))
    if block.startswith("####"):
        return LeafNode("h4", block.strip("#### "))
    if block.startswith("#####"):
        return LeafNode("h5", block.strip("##### "))
    if block.startswith("######"):
        return LeafNode("h6", block.strip("###### "))
    
def block_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

    
def block_code(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def block_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)