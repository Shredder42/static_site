import os
from pathlib import Path
from markdown_blocks import *

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)



'''
Alex written functions

def extract_title(markdown):
    filtered_blocks = markdown_to_blocks(markdown)
    for filtered_block in filtered_blocks:
        if block_to_block_type(filtered_block) == 'heading':
            if filtered_block.startswith('# '):
                return filtered_block.lstrip('# ')
    else:
        raise Exception("No level 1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, 'r') as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    html_page = template.replace('{{ Title }}', title).replace('{{ Content }}', html_node)
    print(os.path.dirname(dest_path))
    out_path = os.path.dirname(dest_path)
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
    with open(dest_path, 'w') as f:
        f.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if filename.endswith('.md'):
                with open(from_path, 'r') as markdown_file:
                    markdown = markdown_file.read()

                with open(template_path, 'r') as template_file:
                    template = template_file.read()

                html_node = markdown_to_html_node(markdown).to_html()

                title = extract_title(markdown)

                html_page = template.replace('{{ Title }}', title).replace('{{ Content }}', html_node)
                if not os.path.isdir(dest_dir_path):
                    os.makedirs(dest_dir_path, exist_ok=True)
                with open(os.path.join(dest_dir_path, filename.replace('.md', '.html')), 'w') as f:
                    f.write(html_page)
            else:
                continue
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
'''
    