import unittest

from text_node import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        tn1 = TextNode("Hello world.", TextType.BOLD)
        tn2 = TextNode("Hello world.", TextType.BOLD)
        self.assertEqual(tn1, tn2)

    def test_not_eq(self):
        tn1 = TextNode("Hello world.", TextType.BOLD)
        tn2 = TextNode("Hello world.", TextType.ITALIC)
        self.assertNotEqual(tn1, tn2)

    def test_props_default_None(self):
        tn = TextNode("Hello world.", TextType.BOLD)
        self.assertIsNone(tn.props)

    def test_tn_to_html_text(self):
        node = TextNode("Hello world.", TextType.TEXT)
        expected_html = "Hello world."
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)

    def test_tn_to_html_bold(self):
        node = TextNode("Hello world.", TextType.BOLD, {"class":"fw-900"})
        expected_html = "<b class=\"fw-900\">Hello world.</b>"
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)

    def test_tn_to_html_italic(self):
        node = TextNode("Hello world.", TextType.ITALIC, {"class":"fw-900"})
        expected_html = "<i class=\"fw-900\">Hello world.</i>"
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)

    def test_tn_to_html_code(self):
        node = TextNode("Boot Dev", TextType.CODE, "pyTHon")
        expected_html = "<pre><code class=\"language-python\">Boot Dev</code></pre>"
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)

    def test_tn_to_html_link(self):
        node = TextNode("Boot Dev", TextType.LINK, "https://www.boot.dev")
        expected_html = "<a href=\"https://www.boot.dev\">Boot Dev</a>"
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)

    def test_tn_to_html_image(self):
        node = TextNode("Boot Dev", TextType.IMAGE, "boot_dev.png")
        expected_html = "<img src=\"boot_dev.png\" alt=\"Boot Dev\"></img>"
        self.assertEqual(node.to_leaf_node().to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
