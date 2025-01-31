import unittest

from html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1= HTMLNode("p", None, "Hello World", None)
        node2= HTMLNode("p", None, "Hello World", None)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1= HTMLNode("p", None, "Hello World", None)
        node2= HTMLNode("li", None, "Hello World", None)
        self.assertNotEqual(node1, node2)
        print(node2)

    def test_props_to_html(self):
        sample_props= {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        expected_html= ' href="https://www.google.com" target="_blank"'
        node= HTMLNode(props=sample_props)
        self.assertEqual(node.props_to_html(), expected_html)

    def test_no_props_to_html(self):
        node= HTMLNode("p", None, "Hello World", None)
        expected_html = ""
        self.assertEqual(node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
