import unittest

from block_markdown import BlockMarkdown


class TestBlockMarkdown(unittest.TestCase):
    
    def test_blocks(self):
        text = """
            This is **bolded** paragraph

                This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line
            Something new

                * This is a list
            * with items
            """
        md = BlockMarkdown(text)
        print(md.create_blocks())
        pass
        
if __name__ == "__main__":
    unittest.main()
