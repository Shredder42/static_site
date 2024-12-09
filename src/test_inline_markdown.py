import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [
                                                    TextNode("This is text with a ", TextType.TEXT),
                                                    TextNode("code block", TextType.CODE),
                                                    TextNode(" word", TextType.TEXT),
                                                ])
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [
                                                    TextNode("This is text with a ", TextType.TEXT),
                                                    TextNode("italic", TextType.ITALIC),
                                                    TextNode(" word", TextType.TEXT),
                                                ])
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
                                                    TextNode("This is text with a ", TextType.TEXT),
                                                    TextNode("bold", TextType.BOLD),
                                                    TextNode(" word", TextType.TEXT),
                                                ])
    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
    def test_split_nodes_delimiter_link(self):
        node = TextNode("This is text with a link", TextType.LINK, "www.mlb.com")
        self.assertEqual(split_nodes_delimiter([node], None, TextType.LINK), [
                                                    TextNode("This is text with a link", TextType.LINK, "www.mlb.com")
                                                ])