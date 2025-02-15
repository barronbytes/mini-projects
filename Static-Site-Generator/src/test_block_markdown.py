import unittest

from block_markdown import BlockMarkdown


class TestBlockMarkdown(unittest.TestCase):
    
    def test_blocks(self):
        text = """
            One

                One One
            Two Two
            Three Three

                One One One
            Two Two Two


            Now

            Done
        """
        md = BlockMarkdown(text)
        print(md.create_blocks())
        pass
        
if __name__ == "__main__":
    unittest.main()
