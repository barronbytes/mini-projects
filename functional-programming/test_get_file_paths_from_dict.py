# Created on: 06-01-2024

from get_file_paths_from_dict import *

dict1 = {
    "Boot.Dev": "README.md",
    "Learning_to_Code": {
        "README.md": None,
        "Functional": {
            "numbers.py": None,
            "sum.py": None
        }
    }
}

paths1 = [
    '/Boot.Dev/README.md',
    '/Learning_to_Code/README.md',
    '/Learning_to_Code/Functional/numbers.py',
    '/Learning_to_Code/Functional/sum.py'
]

dict2 = {
    "Documents": {
        "resume.docx": None,
        "cover_letter.docx": None
    },
    "Pictures": {
        "photo.jpg": None,
        "logo.png": None
    }
}

paths2 = [
    '/Documents/resume.docx',
    '/Documents/cover_letter.docx',
    '/Pictures/photo.jpg',
    '/Pictures/logo.png'
]

submit_cases = [
    (dict1, paths1),
    (dict2, paths2),
]

def test(input, expected_output):
    print("------------------------------")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = get_file_paths_from_dict(input)
    outcome = result == expected_output
    print(f"Actual output: {result}")
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
