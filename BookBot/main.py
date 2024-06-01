# Created on: 05-18-2024

import string

class BookBot:
    ''' Class to analyze the content of a book from a text file '''

    def __init__(self, file_path):
        ''' Initialize BookBot object with a file path '''
        self.file_path = file_path

    def get_book(self):
        ''' Read the book content from the file path
            Returns:
                str: The entire book content if found, else None
        '''
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as f:
                return f.read()        
        except FileNotFoundError:
            return None
    
    @staticmethod
    def get_word_count(book):
        ''' Get the word count of the book content
            Parameters:
                book (str): The entire book content
            Returns:
                int: Number of words in the book
        '''
        return len(book.split())
    
    @staticmethod
    def get_letters_unsorted(book):
        ''' Count the occurences of letters in a book
            Parameters:
                book (str): The entire book content
            Returns:
                dict: The keys are alphabetical letters, the values are integer counts
        '''
        alphabet = tuple(string.ascii_lowercase)
        letters_lowercase = book.lower()
        return {letter: letters_lowercase.count(letter) for letter in alphabet}
    
    @staticmethod
    def get_letters_sorted(unsorted_letters):
        ''' Sort the occurences of letters in a book by frequency used
            Parameters:
                unsorted_letters (dict): The keys are alphabetical letters, the values are integer counts
            Returns:
                dict: The keys are numerically sorted letters, the values are integer counts
        '''
        return dict(sorted(unsorted_letters.items(), key=lambda item: item[1], reverse=True))
    
    def generate_report(self, book_found, word_count, letters_sorted):
        ''' Print report of book contents
            Parameters:
                book_found (bool): True if file found, False if file not found
                word_count (int): Number of words in book, 0 if file not found
                letters (dict): Key-value pairs are letters and integers sorted by letter use in book
                                {} if word count is zero or file not found
        '''
        print(f"--- Begin report for filename: {self.file_path} ---")
        print(f"Book found?: {'no' if not book_found else 'yes'}")
        print(f"Word count: {word_count} \n")
        print("\n".join(f"The '{letter}' character was found {letters_sorted[letter]} times" for letter in letters_sorted))
        print(f"--- End report ---")

def main():
    ''' Main function to read a book file and generate a report '''
    file_path = "books/frankenstein.txt"
    book_bot = BookBot(file_path)
    book = book_bot.get_book()
    book_found = True if (book is not None) else False
    word_count = BookBot.get_word_count(book) if book_found else 0
    letters_unsorted = BookBot.get_letters_unsorted(book) if (book is not None) else {}
    letters_sorted = BookBot.get_letters_sorted(letters_unsorted) if (len(letters_unsorted) != 0) else {}
    book_bot.generate_report(book_found, word_count, letters_sorted)

if __name__ == "__main__":
    main()
