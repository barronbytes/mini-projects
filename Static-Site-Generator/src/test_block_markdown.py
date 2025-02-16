import unittest

from block_markdown import BlockMarkdown, BlockType


class TestBlockMarkdown(unittest.TestCase):

    def test_create_blocks_empty(self):
        text = """
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ["\n"]
        )

    def test_create_blocks_1(self):
        text = """
            One
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ["One"]
        )

    def test_create_blocks_2(self):
        text = """
            One
            Two

            One One
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ["One\nTwo", "One One"]
        )
    
    def test_create_blocks_5(self):
        text = """
            Wake Up
            Make Cereal

            * Milk
            * Cereal
            * Banana

            What Next?
            Get To Work
            

            * Get Dressed
                * Drive To Work.

            Wait To Leave Home.
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ['Wake Up\nMake Cereal', '* Milk\n* Cereal\n* Banana', 'What Next?\nGet To Work', '* Get Dressed\n* Drive To Work.', 'Wait To Leave Home.']
        )

    def test_block_type_h1(self):
        text = "# Pay Attention"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Pay Attention", BlockType.H1)
        )

    def test_block_type_h4(self):
        text = "#### Pay Attention"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Pay Attention", BlockType.H4)
        )

    def test_block_type_code_quote(self):
        text = "> Progress is progress."
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Progress is progress.", BlockType.QUOTE)
        )

    def test_block_type_code_ul_bullet(self):
        text = "* Yogurt"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Yogurt", BlockType.UL)
        )

    def test_block_type_code_ul_dash(self):
        text = "- Yogurt"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Yogurt", BlockType.UL)
        )

    def test_block_type_code_ol(self):
        text = "1. Yams"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("Yams", BlockType.OL)
        )

    def test_block_type_code(self):
        text = "`print(\"hello\")`"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("print(\"hello\")", BlockType.CODE)
        )

    def test_block_type_code_multiline(self):
        text = """
        ```python
        print(\"world\")
        ```
        """
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("python\n        print(\"world\")\n        ", BlockType.CODE)
        )

    def test_block_type_code_paragraph(self):
        text = "hello folks"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            ("hello folks", BlockType.PARAGRAPH)
        )


if __name__ == "__main__":
    unittest.main()
