import unittest

from text_node import TextNode, TextType
from inline_markdown import InlineMarkdown


class TextInlineMarkdown(unittest.TestCase):
    def test_instance_fields(self):
        text_expected = "Something **bold** and *italic* in my __data__ today."
        md = InlineMarkdown(text_expected)
        self.assertEqual(md.text, text_expected)

    def test_delim_bold(self):
        text = "This has **bold** text **twice** inside."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text ", TextType.TEXT),
                TextNode("twice", TextType.BOLD),
                TextNode(" inside.", TextType.TEXT),
            ]
        )

    def test_delim_bold_italic(self):
        text = "This has **bold** and _italic_ inside."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" inside.", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()
