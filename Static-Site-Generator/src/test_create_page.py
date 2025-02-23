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

    def test_create_page(self):
        md, html = CreatePage.read_md_and_template()
        print(f"\n\nMarkdown:\n{md}\n\nHTML Template:\n{html}")
        pass
