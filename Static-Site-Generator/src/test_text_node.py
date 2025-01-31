import unittest

from text_node import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        tn1 = TextNode("Hello world.", TextType.BOLD)
        tn2 = TextNode("Hello world.", TextType.BOLD)
        self.assertEqual(tn1, tn2)

    def test_not_eq(self):
        tn1 = TextNode("Hello world.", TextType.BOLD)
        tn2 = TextNode("Hello world.", TextType.CODE)
        self.assertNotEqual(tn1, tn2)

    def test_url_default_None(self):
        tn1 = TextNode("Hello world.", TextType.BOLD)
        self.assertIsNone(tn1.url)

if __name__ == "__main__":
    unittest.main()
