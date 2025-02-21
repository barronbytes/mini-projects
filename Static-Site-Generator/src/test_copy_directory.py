import unittest
import os

from copy_directory import CopyDirectory


class TestLeafNode(unittest.TestCase):

    def setUp(self):
        self.brain = CopyDirectory("static", "public")

    def test_eq(self):
        other = CopyDirectory("static", "public")
        self.assertEqual(self.brain, other)

    def test_not_eq(self):
        other = CopyDirectory("source_dir_name", "destination_dir_name")
        self.assertNotEqual(self.brain, other)

    def test_is_both_found(self):
        self.assertEqual(
            self.brain.is_both_found(),
            True
        )

    def test_wipe_destination(self):
        self.brain.wipe_destination()
        self.assertTrue(os.path.isdir(self.brain.destination))
        self.assertEqual(len(os.listdir(self.brain.destination)), 0)

    def test_copy_contents(self):
        self.brain.copy_parent_dir()
        pass


if __name__ == "__main__":
    unittest.main()
