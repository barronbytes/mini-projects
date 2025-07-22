# Created on: 05-29-2024

from get_filename_extension import *

submit_cases = [
    ("business_pitch.ppt", "Unknown"),
    ("hello_world.txt", "Text"),
    ("forex_trading.java", "Java"),
    ("data_science.py", "Python"),
]

def test(input, expected_output):
    print("------------------------------")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = get_filename_extension(input)
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