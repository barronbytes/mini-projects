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
            (
                False,
                [BlockType.PARAGRAPH, BlockType.PARAGRAPH],
                ["Almost done.", "Not really."],
            )
        )

    def test_block_text_headers(self):
        block_md_text = """
        # Almost Done

        ## Not Really
        """
        md = BlockMarkdown(block_md_text)
        self.assertEqual(
            md.to_block_text(),
            (
                False,
                [BlockType.H1, BlockType.H2],
                ["Almost Done", "Not Really"],
            )
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
            (
                False,
                [BlockType.H1, BlockType.QUOTE],
                ["Almost Done", "<p>Not</p><p>Really</p>"],
            )
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
            (
                False,
                [BlockType.UL, BlockType.OL],
                ["<li>Almost done</li>", "<li>Not</li><li>Really</li>"],
            )
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
            (
                True,
                [BlockType.CODE],
                ['        def is_winner(num: int) -> None:\n            if num == 2:\n                print("You won.")\n            else:\n                print("You lost.")'],
            )
        )

    def test_html_code(self):
        text = """```python
        def is_winner(num: int) -> None:
            if num == 2:
                print("You won.")
            else:
                print("You lost.")
        ```"""
        md = BlockMarkdown(text)
        self.assertEqual(
            md.to_html(),
'''<div><pre><code class=\"language-python\">
        def is_winner(num: int) -> None:
            if num == 2:
                print("You won.")
            else:
                print("You lost.")
</code></pre></div>''',
        )


    def test_html_capstone(self):
        text = """
        # Boot.dev

        ## Backend Developer Roadmap

        The initial modules on
        [boot.dev](https://boot.dev) teach
        the following:

        > Linux
        > Git
        > Python

        I have completed these projects:

        1. BookBot
        2. Asteroids

        I want to attend these conferences:

        * Dev Nexus
        * Atlanta Cloud Conference
        * RenderATL
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.to_html(),
            '<div><h1>Boot.dev</h1><h2>Backend Developer Roadmap</h2><p>The initial modules on <a href="https://boot.dev">boot.dev</a> teach the following:</p><blockquote><p>Linux</p><p>Git</p><p>Python</p></blockquote><p>I have completed these projects:</p><ol><li>BookBot</li><li>Asteroids</li></ol><p>I want to attend these conferences:</p><ul><li>Dev Nexus</p><li>Atlanta Cloud Conference</p><li>RenderATL</li></ul></div>',
        )


if __name__ == "__main__":
    unittest.main()
