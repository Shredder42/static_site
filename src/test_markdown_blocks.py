import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type

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

