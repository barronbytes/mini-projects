import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init_value_error_of_tag(self):
        with self.assertRaises(ValueError) as context:
            LeafNode(None, "Hello World")
        self.assertEqual(str(context.exception), "Invalid parameter(s): tag=None")

    def test_init_value_error_of_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "Invalid parameter(s): value=None")

    def test_init_value_error_of_tag_and_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode(None, None)
        self.assertEqual(str(context.exception), "Invalid parameter(s): tag=None, value=None")

    def test_eq(self):
        node1 = LeafNode("p", "Hello World", None)
        node2 = LeafNode("p", "Hello World", None)
        self.assertEqual(node1, node2)
    
    def test_to_html_no_url(self):
        node = LeafNode("p", "Paragraph text.")
        expected_HTML = "<p>Paragraph text.</p>"
        self.assertEqual(node.to_html(), expected_HTML)

    def test_to_html_url(self):
        node = LeafNode("a", "Sign Up!", {"href": "https://www.google.com"})
        expected_HTML = '<a href="https://www.google.com">Sign Up!</a>'
        self.assertEqual(node.to_html(), expected_HTML)      

if __name__ == "__main__":
    unittest.main()
