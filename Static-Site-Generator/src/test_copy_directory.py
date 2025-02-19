import unittest

from copy_directory import CopyDirectory


class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        entity1 = CopyDirectory("from_here", "to_here")
        entity2 = CopyDirectory("from_here", "to_here")
        self.assertEqual(entity1, entity2)

    def test_not_eq(self):
        entity1 = CopyDirectory("from_here", "to_here")
        entity2 = CopyDirectory("from_here", "destination")
        self.assertNotEqual(entity1, entity2)

    def test_is_both_found(self):
        brain = CopyDirectory("static", "public")
        self.assertEqual(
            brain.is_both_found(),
            True
        )

if __name__ == "__main__":
    unittest.main()
