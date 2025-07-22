# Created on: 05-18-2024

import unittest
from main import BookBot

class TestBookBot(unittest.TestCase):
    ''' Unit tests for the BookBot class '''

    def setUp(self):
        ''' Set up file paths and contents for testing '''
        self.file_path_not_found = "books/not_real_path.txt"
        self.file_path_empty = "books/empty.txt"
        self.file_path_alice = "books/aliceinwonderland.txt"

        with open(self.file_path_alice, mode="r", encoding="utf-8") as f:
            self.book_alice = f.read()

    def test_get_book_file_not_found(self):
        ''' Test get_book method with a non-existent file path '''
        book_bot = BookBot(self.file_path_not_found)
        book = book_bot.get_book()
        self.assertIsNone(book)

    def test_get_book_empty(self):
        ''' Test get_book method with an empty file '''
        book_bot = BookBot(self.file_path_empty)
        book = book_bot.get_book()
        self.assertEqual(book, "")

    def test_get_book_alice(self):
        ''' Test get_book method with Alice in Wonderland file '''
        book_bot = BookBot(self.file_path_alice)
        book = book_bot.get_book()
        self.assertEqual(book, self.book_alice)

    def test_get_word_count(self):
        ''' Test get_word_count method with a sample sentence '''
        book = "This is a sentence with seven words."
        word_count_actual = BookBot.get_word_count(book)
        word_count_expected = len(book.split())
        self.assertEqual(word_count_actual, word_count_expected)

if __name__ == "__main__":
    unittest.main()
