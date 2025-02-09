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
            md.create_group_nodes(md.find_matches()),
            [
                (16, 37, TextNode("Wicked", TextType.IMAGE, "wicked.png")),
                (42, 67, TextNode("Twisters", TextType.IMAGE, "twisters.png")),
            ]
        )

    def test_match_link(self):
        text = "I am a [boot.dev](https://boot.dev) member since 2024 and counting."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.create_group_nodes(md.find_matches()),
            [
                (7, 35, TextNode("boot.dev", TextType.LINK, "https://boot.dev")),
            ]
        )

    def test_match_code(self):
        text = "Every coder writes `python print(\"Hello World.\")` at the start."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.create_group_nodes(md.find_matches()),
            [
                (19, 49, TextNode("print(\"Hello World.\")", TextType.CODE, "python")),
            ]
        )

    def test_match_bold_italic(self):
        text = "You **must** know that rules _can be_ broken."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.create_group_nodes(md.find_matches()),
            [
                (4, 12, TextNode("must", TextType.BOLD, None)),
                (29, 37, TextNode("can be", TextType.ITALIC, None)),
            ]
        )

    def test_nodes_bold_italic(self):
        text = "You **must** know that rules _can be_ broken."
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("You ", TextType.TEXT),
                TextNode("must", TextType.BOLD),
                TextNode(" know that rules ", TextType.TEXT),
                TextNode("can be", TextType.ITALIC),
                TextNode(" broken.", TextType.TEXT),
            ]
        )

    def test_nodes_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        md = InlineMarkdown(text)
        self.assertListEqual(
            md.to_text_nodes(),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE, ""),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()
