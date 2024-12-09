import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    def test_extract_markdown_images_extra_spaces(self):
        text = "This is text with a ![rick roll]( https://i.imgur.com/aKaOqIh.gif ) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", " https://i.imgur.com/aKaOqIh.gif "), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def test_extract_markdown_images_image_and_link(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    def test_extract_markdown_links_link_and_image(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and image ![to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev")])