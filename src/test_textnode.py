import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.mlb.com") 
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.mlb.com")
        self.assertEqual(node, node2)
    def test_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a differen node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_diff_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_diff_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.mlb.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.mlb.com")
        self.assertEqual("TextNode(This is a text node, bold text, https://www.mlb.com)", repr(node))        

if __name__ == '__main__':
    unittest.main()