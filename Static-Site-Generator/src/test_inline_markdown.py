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

    def test_delim_code(self):
        text = "Every coder writes `python print(\"Hello World.\")` at the start."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("Every coder writes ", TextType.TEXT),
                TextNode("print(\"Hello World.\")", TextType.CODE, "python"),
                TextNode(" at the start.", TextType.TEXT),
            ]
        )
    
    def test_delim_link(self):
        text = "I am a [boot.dev](https://boot.dev) member since **2024** and counting."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("I am a ", TextType.TEXT),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" member since ", TextType.TEXT),
                TextNode("2024", TextType.BOLD),
                TextNode(" and counting.", TextType.TEXT),
            ]
        )
    
    def test_delim_image(self):
        text = "Look at the ![bird](bird.png) in the air."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("Look at the ", TextType.TEXT),
                TextNode("bird", TextType.IMAGE, "bird.png"),
                TextNode(" in the air.", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()
