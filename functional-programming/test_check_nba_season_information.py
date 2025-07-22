# Created on: 06-02-2024

from check_nba_season_information import *

# Test cases
submit_cases_home_status = [
    (WesternConference.MAVERICKS, {'Team': 'Mavericks', 'Rank': 5, 'Home': 'No'}),
    (WesternConference.LAKERS, {'Team': 'Lakers', 'Rank': 7, 'Home': 'No'}),
    (EasternConference.CELTICS, {'Team': 'Celtics', 'Rank': 1, 'Home': 'Yes'}),
    (EasternConference.KNICKS, {'Team': 'Knicks', 'Rank': 2, 'Home': 'Yes'})
]

submit_cases_opponent_name = [
    (WesternConference.MAVERICKS, {'Team': 'Mavericks', 'Rank': 5, 'Opponent': 'Clippers', 'Opponent Rank': 4}),
    (WesternConference.LAKERS, {'Team': 'Lakers', 'Rank': 7, 'Opponent': 'Nuggets', 'Opponent Rank': 2}),
    (EasternConference.CELTICS, {'Team': 'Celtics', 'Rank': 1, 'Opponent': 'Heat', 'Opponent Rank': 8}),
    (EasternConference.KNICKS, {'Team': 'Knicks', 'Rank': 2, 'Opponent': 'Sixers', 'Opponent Rank': 7})
]

def test(input, expected_output, test_function):
    print("------------------------------")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = test_function(input)
    outcome = result == expected_output
    print(f"Actual output: {result}")
    print(f"Outcome: {'Pass' if outcome else 'Fail'}")
    return outcome

def main():
    home_status_fn = check_nba_season_information(check_home_status)
    opponent_name_fn = check_nba_season_information(check_opponent_name)

    outcomes_home_status = [test(case[0], case[1], home_status_fn) for case in submit_cases_home_status]
    outcomes_opponent_name = [test(case[0], case[1], opponent_name_fn) for case in submit_cases_opponent_name]

    passed_home_status = outcomes_home_status.count(True)
    failed_home_status = outcomes_home_status.count(False)
    result_home_status = "PASS" if failed_home_status == 0 else "FAIL"

    passed_opponent_name = outcomes_opponent_name.count(True)
    failed_opponent_name = outcomes_opponent_name.count(False)
    result_opponent_name = "PASS" if failed_opponent_name == 0 else "FAIL"

    print(f"=============== Home Status Test {result_home_status} ===============")
    print(f"{passed_home_status} passed, {failed_home_status} failed")

    print(f"=============== Opponent Name Test {result_opponent_name} ===============")
    print(f"{passed_opponent_name} passed, {failed_opponent_name} failed")

main()
