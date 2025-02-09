import unittest

from text_node import TextNode, TextType
from inline_markdown import InlineMarkdown


class TextInlineMarkdown(unittest.TestCase):

    def test_instance_fields(self):
        text_expected = "Something **bold** and *italic* in my __data__ today."
        md = InlineMarkdown(text_expected)
        self.assertEqual(md.text, text_expected)

    def test_matches_found_false(self):
        text = "This text has no markup nodes."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.find_matches(),
            []
        )

    def test_match_image(self):
        text = "I did not watch ![Wicked](wicked.png) nor ![Twisters](twisters.png) in theaters."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.create_markup_nodes(md.find_matches()),
            [
                (16, 37, TextNode("Wicked", TextType.IMAGE, "wicked.png")),
                (42, 67, TextNode("Twisters", TextType.IMAGE, "twisters.png")),
            ]
        )

    def test_match_link(self):
        text = "I am a [boot.dev](https://boot.dev) member since 2024 and counting."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.create_markup_nodes(md.find_matches()),
            [
                (7, 35, TextNode("boot.dev", TextType.LINK, "https://boot.dev")),
            ]
        )
    
    @unittest.skip("Skipping this test for now")
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

    @unittest.skip("Skipping this test for now")
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

    @unittest.skip("Skipping this test for now")
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

if __name__ == "__main__":
    unittest.main()
