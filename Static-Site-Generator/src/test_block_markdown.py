import unittest

from block_markdown import BlockMarkdown


class TestBlockMarkdown(unittest.TestCase):

    def test_md_empty(self):
        text = """
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ["\n"]
        )

    def test_md_block1(self):
        text = """
            One
        """
        md = BlockMarkdown(text)
        self.assertEqual(
            md.create_blocks(),
            ["One"]
        )

    def test_md_block2(self):
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
    
    def test_block5(self):
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
        
if __name__ == "__main__":
    unittest.main()
