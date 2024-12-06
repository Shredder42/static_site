import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = HTMLNode('p', 'this is the text', None,{
                                                    "href": "https://www.google.com", 
                                                    "target": "_blank",
                                                }
                        )
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')
    def test_props_to_html_not_eq(self):
        node = HTMLNode('p','this is the text', None, {
                                                    "href": "https://www.google.com", 
                                                    "target": "ghost",
                                                }
                        )
        self.assertNotEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')
    def test_props_to_html_empty(self):
        node = HTMLNode('p', 'this is the text', None)
        self.assertEqual(node.props_to_html(),  '')

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(Tag: p; Value: What a strange world; Children: None; Props: {'class': 'primary'})",
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")
    

if __name__ == '__main__':
    unittest.main()