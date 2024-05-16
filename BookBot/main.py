import string

file_path = "books/frankenstein.txt"
alphabet = tuple(string.ascii_lowercase)

def get_book_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def get_letter_count(content):
    return {letter: content.count(letter) for letter in alphabet}

def sort_letters_by_values(letters):
    return dict(sorted(letters.items(), key= lambda item: item[1] ,reverse= True))

def get_book_report(words, letters):
    print(f"--- Begin report of {file_path} ---")
    print(f"{words} words found in the document \n")
    print("\n".join(f"The '{letter}' character was found {letters[letter]} times" for letter in letters))
    print(f"--- End report ---")

def main():
    content = get_book_content(file_path)
    words_count = len(content.split())
    content_lower = [char for char in content.lower() if char in alphabet]
    letter_count = get_letter_count(content_lower)
    letter_count_sorted = sort_letters_by_values(letter_count)
    get_book_report(words_count, letter_count_sorted)

main()
