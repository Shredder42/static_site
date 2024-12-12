block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        # i reversed the block.strip() line belwo with the if statement below that from the boot_dev solution
        # it was failing one of the tests written the way in the solution
        block = block.strip()    
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("_ "):
        for line in lines:
            if not line.startswith("_ "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph



'''
Alex written fuctions

def markdown_to_blocks(markdown):
    final_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if block and not block.isspace():
            stripped_block = block.strip(' ')
            if stripped_block.startswith('\n'):
                stripped_block = stripped_block.replace('\n', '')
            final_blocks.append(stripped_block)
    return final_blocks

    
def block_to_block_type(block):
    lines = block.split('\n')

    available_headings = ['#' * i + ' ' for i in range(1,7)]
    heading_block = block
    heading_string = ''
    for value in heading_block:
        if value == '#':
            heading_string += value
            heading_block = heading_block[1:]
        elif value == ' ':
            heading_string += value
            break
        else:
            break
    if heading_string in available_headings:
        return 'heading'
    
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    for line in lines:
        if not line.startswith('>'):
            break
    else:
        return 'quote'
    
    for line in lines:
        if not (line.startswith('* ') or line.startswith('_ ')):
            break
    else:
        return 'unordered list'
    
    for line in lines:
        if not (line.startswith(f'{lines.index(line) + 1}. ')):
            break
    else:
        return 'ordered list'
    
    return 'paragraph'
'''