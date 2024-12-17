import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = '''# This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item'''
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', '# This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '# * This is the first list item in a list block\n# * This is a list item\n# * This is another list item'])
    def test_markdown_to_blocks_extra_blank_line(self):
        text = '''# This is a heading


# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item'''
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', '# This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '# * This is the first list item in a list block\n# * This is a list item\n# * This is another list item'])
    def test_markdown_to_blocks_2_extra_blank_lines(self):
        text = '''# This is a heading



# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item'''
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', '# This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '# * This is the first list item in a list block\n# * This is a list item\n# * This is another list item'])
    def test_markdown_to_blocks_block_with_only_whitespace(self):
        text = '''# This is a heading

                    

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item'''
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', '# This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '# * This is the first list item in a list block\n# * This is a list item\n# * This is another list item'])

    def test_block_to_block_type_heading(self):
        text = '''## ghost'''
    def test_block_to_block_type_no_pound_heading(self):
        text = ''' ghost'''
        self.assertEqual(block_to_block_type(text), 'paragraph')
    def test_block_to_block_type_too_many_pound_signs(self):
        text = '''####### ghost'''
        self.assertEqual(block_to_block_type(text), 'paragraph')
    def test_block_to_block_type_code(self):
        text = '''```
ghost
```'''
        self.assertEqual(block_to_block_type(text), 'code')
    def test_block_to_block_type_code_with_heading(self):
        text = '''```
## ghost
```'''
        self.assertEqual(block_to_block_type(text), 'code')
    def test_block_to_block_type_quote(self):
        text = '''>ghost'''
        self.assertEqual(block_to_block_type(text), 'quote')
    def test_block_to_block_type_multi_line_quote(self):
        text = '''>ghost
>alex'''
        self.assertEqual(block_to_block_type(text), 'quote')
    def test_block_to_block_type_incorrect_quote(self):
        text = '''>ghost
* alex'''
        self.assertEqual(block_to_block_type(text), 'paragraph')
    def test_block_to_block_type_uo_list(self):
        text = '''* ghost
* alex'''
        self.assertEqual(block_to_block_type(text), 'unordered_list')
    def test_block_to_block_type_o_list(self):
        text = '''1. ghost
2. alex'''
        self.assertEqual(block_to_block_type(text), 'ordered_list')
    def test_block_to_block_type_out_of_order_list(self):
        text = '''1. ghost
2. alex
4. hannah'''
        self.assertEqual(block_to_block_type(text), 'paragraph')
    def test_block_to_block_type_mixed_list(self):
        text = '''1. ghost
2. alex
_ hannah'''
        self.assertEqual(block_to_block_type(text), 'paragraph')
    def test_block_to_block_type_paragraph(self):
        text = '''ghost'''
        self.assertEqual(block_to_block_type(text), 'paragraph')

#     def test_markdown_to_html_node(self):
#         markdown = '''### *DOGGY!* wings

# ghost is my **dog**### *DOGGY!* wings

# * **alex** is the best

# ```
# ghost.bark()
# alex.soccer()
# ```

# 1. zombie is *here*
# 2. friend with a [link text](https:///url.com)

# >ghost is 
# >the best dog
# '''
#         self.assertEqual(markdown_to_html_node(markdown), '''<div><h3><i>DOGGY!</i> wings</h3><p>ghost is my <b>dog</b>### <i>DOGGY!</i> wings</p><ul><li><b>alex</b> is the best</li></ul><pre><code>
# ghost.bark()
# alex.soccer()
# </code></pre><ol><li>zombie is <i>here</i></li><li>friend with a <a href="https:///url.com">link text</a></li></ol><blockquote>ghost is the best dog</blockquote></div>''')
#     def test_paragraph(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
#         )

#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with *italic* text and `code` here

# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

#     def test_lists(self):
#         md = """
# - This is a list
# - with items
# - and *more* items

# 1. This is an `ordered` list
# 2. with items
# 3. and more items
# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
#         )

#     def test_headings(self):
#         md = """
# # this is an h1

# this is paragraph text

# ## this is an h2
# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
#         )

#     def test_blockquote(self):
#         md = """
# > This is a
# > blockquote block

# this is paragraph text

# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
#         )
