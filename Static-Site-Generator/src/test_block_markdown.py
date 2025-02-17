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
            BlockType.H1
        )

    def test_block_type_h4(self):
        text = "#### Pay Attention"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.H4
        )

    def test_block_type_quote(self):
        text = "> Progress is progress\n> Do not quit."
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.QUOTE
        )

    def test_block_type_ul_bullet(self):
        text = "* Yogurt\n* Oatmeal"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.UL
        )

    def test_block_type_ul_dash(self):
        text = "- Yogurt\n- Oatmeal"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.UL
        )

    def test_block_type_ol(self):
        text = "1. Yams\n2. Beef"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.OL
        )

    def test_block_type_code(self):
        text = "`print(\"hello\")`"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.CODE
        )

    def test_block_type_code_multiline(self):
        text = """
        ```python
        print(\"world\")
        ```
        """
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.CODE
        )

    def test_block_type_code_paragraph(self):
        text = "hello folks"
        self.assertEqual(
            BlockMarkdown.block_type(text),
            BlockType.PARAGRAPH
        )

    def test_map_paragraph(self):
        block_md_text = """
            I am *almost* done.

            Not
            really.
        """
        mdd = BlockMarkdown(block_md_text)
        print(mdd.to_html_nodes())
        pass


if __name__ == "__main__":
    unittest.main()
