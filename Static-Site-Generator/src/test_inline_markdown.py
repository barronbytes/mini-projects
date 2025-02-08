import unittest

from inline_markdown import InlineMarkdown


class TextInlineMarkdown(unittest.TestCase):
    def test_instance_fields(self):
        text_expected = "Something **bold** and *italic* in my __data__ today."
        md = InlineMarkdown(text_expected)
        self.assertEqual(md.text, text_expected)
        print(md.to_text_nodes())

if __name__ == "__main__":
    unittest.main()
