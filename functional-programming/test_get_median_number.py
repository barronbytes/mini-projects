# Created on: 05-29-2024

from get_median_number import *

submit_cases = [
    ([], None),
    ([10, 2, 8, 4, 6, 12], 7.0),
    ([15, 3, 7, 9, 11], 9),
    ([3, 1, 7], 3)
]

def test(input, expected_output):
    print("------------------------------")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = get_median_number(input)
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