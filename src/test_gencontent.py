import unittest

from gencontent import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        markdown = markdown = '''# Tolkien Fan Club

        **I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien'''
        self.assertEqual(extract_title(markdown), "Tolkien Fan Club")


class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass