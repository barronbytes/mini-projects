import unittest

from parent_node import ParentNode
from leaf_node import LeafNode


class TestParentNode(unittest.TestCase):
    def test_init_value_error_of_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("ul", None)
        self.assertEqual(str(context.exception), "Invalid parameter(s): children=None")

    def test_init_value_error_of_tag_and_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, None)
        self.assertEqual(str(context.exception), "Invalid parameter(s): tag=None, children=None")

    def test_to_html_level_one(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Python"),
                LeafNode(None, " is considered "),
                LeafNode("i", "easy"),
                LeafNode(None, " to learn."),
            ],
        )
        expected_html = "<p><b>Python</b> is considered <i>easy</i> to learn.</p>"
        print(node)
        self.assertEqual(node.to_html(), expected_html)
        pass

if __name__ == "__main__":
    unittest.main()
