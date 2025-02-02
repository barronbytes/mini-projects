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
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_level_one_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Python", {"class": "fw-900"}), # props: should be a dictionary
                LeafNode(None, " is considered "),
                LeafNode("i", "easy"),
                LeafNode(None, " to learn."),
            ],
            {"class": "grid"},  # props: should be a dictionary
        )
        expected_html = "<p class=\"grid\"><b class=\"fw-900\">Python</b> is considered <i>easy</i> to learn.</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_level_two(self):
        grandchild_node = LeafNode("li", "get started")
        child_node = ParentNode("ul", [grandchild_node], {"class": "col-3"})
        parent_node = ParentNode("div", [child_node], {"class": "grid"})
        expected_html = "<div class=\"grid\"><ul class=\"col-3\"><li>get started</li></ul></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
