from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextType, TextNode

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
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

markdown = '''### *My DOGGY!* 

ghost is my **dog**### *DOG!* bone

* **ghost** is the best

and here is an image ![image text](path/to/image.png)

```
ghost.bark()
alex.soccer()
```
1. zombie is *here*
2. friend with a [link text](https:///url.com)

>ghost is 
>the best dog'''
# markdown = '''### heading'''
# print(markdown_to_html_node(markdown).to_html())

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

in the boot dev code they never run .to_html() as far as I can tell
but then I don't know how they convert to the html
my output shows html nodes - not the formatted html with tags that they get
(and was what I was going for)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        nodes.append(block_to_node(block, block_type))
    final_node = ParentNode('div', nodes)
    return final_node.to_html()

def block_to_node(block, block_type):
    if block_type == block_type_quote:
        return quote_html_node(block)
    elif block_type == block_type_ulist:
        return list_html_node(block, block_type_ulist)
    elif block_type == block_type_olist:
        return list_html_node(block, block_type_olist)
    elif block_type == block_type_code:
        return code_html_node(block)
    elif block_type == block_type_heading:
        return heading_html_node(block)
    elif block_type == block_type_paragraph:
        return paragraph_html_node(block)

def quote_html_node(block):
    quote_lines = block.split('\n')
    html_quote = []
    for quote_line in quote_lines:
        html_nodes = text_to_children(quote_line[1:])
        html_quote.extend(html_nodes)
    return ParentNode('blockquote', html_quote)

def heading_html_node(block):
    pound_signs, block_text = block.split(' ', 1)
    heading_value = pound_signs.count('#')
    html_nodes = text_to_children(block_text)
    return ParentNode(f'h{heading_value}', html_nodes)   

def list_html_node(block, list_type):
    if list_type == 'ordered_list':
        list_tag = 'ol'
    if list_type == 'unordered_list':
        list_tag = 'ul'
    list_items = block.split('\n')
    html_list_items = []
    for list_item in list_items:
        text = list_item.split(' ', 1)[1]
        html_nodes = text_to_children(text)
        html_list_items.append(ParentNode('li', html_nodes))
    return ParentNode(list_tag, html_list_items)

def code_html_node(block):
    code_text = block.strip('```')
    return ParentNode('pre', [LeafNode('code', code_text)])

def paragraph_html_node(block):
    html_nodes = text_to_children(block)
    return ParentNode('p', html_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

'''