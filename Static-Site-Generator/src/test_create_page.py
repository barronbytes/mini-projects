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
