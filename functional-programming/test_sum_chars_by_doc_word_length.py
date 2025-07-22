# Created on: 05-30-2024

from sum_chars_by_doc_word_length import *

submit_cases = [
    ("", 0),
    ("Python is amazing. It allows for simple and powerful programming. Explore its features!", 62),
    ("Basketball is fun. It helps build teamwork and discipline. Enjoy the game!", 49),
    ("Hello world!", 11),
]

def test(input, expected_output):
    print("------------------------------")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = sum_chars_by_doc_word_length(input)
    outcome = result == expected_output
    print(f"Outcome: {'Pass' if outcome else 'Fail'}")
    return outcome

def main():
    outcomes = [test(*submit_case) for submit_case in submit_cases]
    passed = outcomes.count(True)
    failed = outcomes.count(False)
    result = "PASS" if failed == 0 else "FAIL"
    print(f"=============== {result} ===============")
    print(f"{passed} passed, {failed} failed")

main()