import unittest
from etl_transform import Transform


class TestTransform(unittest.TestCase):
    def setUp(self):
        self.reviews = [
            "this ring smells weird, don't recomend",
            "I love this ring, I use it all the time when working out.",
            "I will never buy another brand again, I love this ring",
            "It's an ok ring. Some features could be better but for the price its fine.",
            "its a ring",
            "Bought this ring and it came broken. rip-off."
        ]
        self.all_labels = { "negative", "neutral", "positive", "irrelevant" }


    def test_empty_error(self):
        self.assertTrue(Transform.check_errors([]))


    def test_type_error(self):
        self.assertTrue(Transform.check_errors([1, 2]))


    def test_openai_response(self):
        print("\nType 'rings' below to properly run the program for a test file.")
        open_ai_response = Transform.prompt_mapper(self.reviews) # string value
        sentiments = Transform.aggregation(open_ai_response) # uses regex -> dict
        response_keys = set(sentiments.keys())
        self.assertTrue(response_keys.issubset(self.all_labels))
