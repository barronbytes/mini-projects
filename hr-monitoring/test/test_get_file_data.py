import unittest
from get_file_data import GetFileData


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.root_dir = GetFileData.root_dir()
        self.files = ['phase0.txt', 'phase1.txt', 'phase2.txt', 'phase3.txt']
    
    def test_root_dir(self):
        self.assertEqual(self.root_dir, ".")

    def test_get_data_files(self):
        expected_files = self.files
        self.assertListEqual(GetFileData.get_data_files(self.root_dir), expected_files)

    def test_select_data_file(self):
        indices = [n for n in range(0, len(self.files))]
        index = GetFileData.select_data_file(self.files)
        self.assertTrue(index in indices)


if __name__ == "__main__":
    unittest.main()