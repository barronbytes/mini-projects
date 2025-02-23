import unittest

from create_page import CreatePage


class TestCreatePage(unittest.TestCase):

    def test_title_present(self):
        markdown = """
        # Almost Done

        ## Not Really
        """
        header = CreatePage.extract_title(markdown)
        self.assertEqual(
            header,
            "Almost Done"
        )

    def test_title_absent(self):
        markdown = """
        ### Almost Done

        ## Not Really
        """
        with self.assertRaises(ValueError):
            CreatePage.extract_title(markdown)

    def test_split_markdown_parts(self):
        markdown = """
        ### Almost Done

        ```
        def is_ready():
            pass
        ```
        ## Not Really
        """
        parts = CreatePage.split_markdown_parts(markdown)
        self.assertEqual(
            CreatePage.split_markdown_parts(markdown),
            ['\n        ### Almost Done\n\n        ', '```\n        def is_ready():\n            pass\n        ```', '\n        ## Not Really\n        '],            
        )

    def test_create_page(self):
        CreatePage.create_page()
        #md, html = CreatePage.read_md_and_template()
        #print(f"\n\nMarkdown:\n{md}\n\nHTML Template:\n{html}")
        pass
