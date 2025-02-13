from htmlnode import *
from split_nodes_delimiter import *
from markdown_to_blocks import *

def markdown_to_html_node(markdown):
    children = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            children.append(block_heading(block))
        if block_type == "unordered list" or block_type == "ordered_list":
            children.append(block_list(block))
        if block_type == "code":
            children.append(block_code(block))
        if block_type == "quote":
            children.append(block_quote(block))
        if block_type == "paragraph":
            children.append(block_paragraph(block))
        
    return HTMLNode("div", None, children, None)
        
            
def block_heading(block):
    if block.startswith("#"):
        return HTMLNode("h1", block.strip("#"), None, None)
    if block.startswith("##"):
        return HTMLNode("h2", block.strip("##"), None, None)
    if block.startswith("###"):
        return HTMLNode("h3", block.strip("###"), None, None)
    if block.startswith("####"):
        return HTMLNode("h4", block.strip("####"), None, None)
    if block.startswith("#####"):
        return HTMLNode("h5", block.strip("#####"), None, None)
    if block.startswith("######"):
        return HTMLNode("h6", block.strip("######"), None, None)
    
def block_list(block):
    children = []
    lines = block.split("\n")
    if block.startswith("* ") or block.startswith("- "):
        children = [HTMLNode("li", None, [HTMLNode(None, line, None, None)], None) for line in lines]
        return HTMLNode("u1", None, children, None)
    if block.startswith(f"{1}. "):
        children = [HTMLNode("li", None, [HTMLNode(None, line, None, None)], None) for line in lines]
        return HTMLNode("o1", None, children, None)
    
def block_code(block):
    children = []
    children.append(HTMLNode("code", block, None, None))
    return HTMLNode("pre", None, children, None)

def block_quote(block):
    return HTMLNode("blockquote", block, None, None)

def block_paragraph(block):
    return HTMLNode("p", block, None, None)