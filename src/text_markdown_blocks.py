import unittest

from markdown_blocks import markdown_to_blocks

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


