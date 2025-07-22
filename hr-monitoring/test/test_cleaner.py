import unittest
from cleaner import Cleaner


class TestCleaner(unittest.TestCase):

    def test_is_list(self):
        data = []
        self.assertTrue(Cleaner(data).is_list())

    def test_data_not_list(self):
        data = "Hello World"
        self.assertEqual(Cleaner(data).brain(), None)

    def test_data_list_empty(self):
        data = []
        self.assertEqual(Cleaner(data).brain(), None)

    def test_data_list_letters(self):
        data = ["  Hello  ", "  World  \n"]
        self.assertEqual(Cleaner(data).brain(), None)

    def test_data_list_numbers_1(self):
        data_1 = ["1\n", "\n", "3\n", "4\n", "5\n", "\n", "7\n"]
        data_2 = ["1\n", "NO DATA\n", "  3  \n", "4\n", "5\n", "NO DATA\n", "7\n"]
        data_expected = [1, 3, 4, 5, 7]
        self.assertListEqual(Cleaner(data_1).brain(), data_expected)
        self.assertListEqual(Cleaner(data_2).brain(), data_expected)


if __name__ == "__main__":
    unittest.main()