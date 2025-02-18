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

    def test_block_type_paragraph(self):
        text = "hello folks"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.PARAGRAPH
        )

    def test_block_type_h1(self):
        text = "# Pay Attention"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.H1
        )

    def test_block_type_h4(self):
        text = "#### Pay Attention"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.H4
        )

    def test_block_type_quote(self):
        text = "> Progress is progress\n> Do not quit."
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.QUOTE
        )

    def test_block_type_ul_bullet(self):
        text = "* Yogurt\n* Oatmeal"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.UL
        )

    def test_block_type_ul_dash(self):
        text = "- Yogurt\n- Oatmeal"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.UL
        )

    def test_block_type_ol(self):
        text = "1. Yams\n2. Beef"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.OL
        )

    def test_block_type_code(self):
        text = "`print(\"hello\")`"
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.CODE
        )

    def test_block_type_code_multiline(self):
        text = """
        ```python
        print(\"world\")
        ```
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.block_type(text),
            BlockType.CODE
        )

    def test_block_text_paragraphs(self):
        block_md_text = """
        Almost done.

        Not
        really.
        """
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            ["Almost done.", "Not really."]
        )

    def test_block_text_headers(self):
        block_md_text = """
        # Almost Done

        ## Not Really
        """
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            ["Almost Done", "Not Really"]
        )

    def test_block_text_quotes(self):
        block_md_text = """
        # Almost Done

        > Not
        > Really
        """
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            ["Almost Done", "Not<br>Really"]
        )

    def test_block_text_lists(self):
        block_md_text = """
        * Almost done

        1. Not
        2. Really
        """
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            ["<li>Almost done</li>", "<li>Not</li><li>Really</li>"]
        )

    def test_block_text_code(self):
        block_md_text = """```python
        def is_winner(num: int) -> None:
            if num == 2:
                print("You won.")
            else:
                print("You lost.")
        ```"""
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            ['        def is_winner(num: int) -> None:\n            if num == 2:\n                print("You won.")\n            else:\n                print("You lost.")']
        )


if __name__ == "__main__":
    unittest.main()
