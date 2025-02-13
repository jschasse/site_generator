

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block.strip()

    for block in blocks:
        if block == "":
            continue
        else:
            filtered_blocks.append(block)
            
    return filtered_blocks
    
def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if block.startswith(">"):
        for line in lines:
            if line.startswith(">"):
                continue
            else:
                return "paragraph"
        return "quote"
    if block.startswith("* "):
        for line in lines:
            if line.startswith("* "):
                continue
            else:
                return "paragraph"
        return "unordered_list"
    if block.startswith("- "):
        for line in lines:
            if line.startswith("- "):
                continue
            else:
                return "paragraph"
        return "unordered_list"
    i = 1
    if block.startswith(f"{i}. "):
        for line in lines:
            if line.startswith(f"{i}. "):
                i += 1
                continue
            else:
                return "paragraph"
        
        return "ordered_list"    
    return "paragraph"