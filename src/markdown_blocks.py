def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks






# Alex written fuctions

# def markdown_to_blocks(markdown):
#     final_blocks = []
#     blocks = markdown.split('\n\n')
#     for block in blocks:
#         if block and not block.isspace():
#             stripped_block = block.strip(' ')
#             if stripped_block.startswith('\n'):
#                 stripped_block = stripped_block.replace('\n', '')
#             final_blocks.append(stripped_block)
#     return final_blocks
