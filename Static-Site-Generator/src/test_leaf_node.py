import unittest

from leaf_node import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "Hello World", None)
        node2 = LeafNode("p", "Hello World", None)
        self.assertEqual(node1, node2)
    
    def test_to_html_no_url(self):
        node = LeafNode("p", "Paragraph text.")
        expected_HTML = "<p>Paragraph text.</p>"
        self.assertEqual(node.to_html(), expected_HTML)
        print(node.to_html())

    def test_to_html_url(self):
        node = LeafNode("a", "Sign Up!", {"href": "https://www.google.com"})
        expected_HTML = '<a href="https://www.google.com">Sign Up!</a>'
        self.assertEqual(node.to_html(), expected_HTML)
        print(node.to_html())        

if __name__ == "__main__":
    unittest.main()
