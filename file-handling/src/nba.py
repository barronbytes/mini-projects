import os
import csv
import json
import copy


# CSV -> read, update -> create JSON
src_dir = os.path.dirname(os.path.relpath(__file__))
csv_input_path = os.path.join(src_dir, "../data_csv/nba.csv")
csv_output_path = os.path.join(src_dir, "../data_csv/nba_new.csv")
json_output_path = os.path.join(src_dir, "../data_json/nba_new.json")


# deserialize data (read file)
def read_data(file_path: str) -> dict:
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


# update data
def update_data(data: list[list[str]]) -> list[list[str]]:
    new_row = ["San Antonio Spurs", "West", "5"]
    data.append(new_row)
    return data


# serialize data (create file)
def create_data(data: list[list[str]], file_path: str) -> None:
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# convert file type
def map_to_json(data: dict, file_path: str) -> None:
    headers = data[0]
    rows = data[1:]
    json_data = {"nba_teams": {}}
    for idx, row in enumerate(rows, start=1):  # start with index 1 for team ids
        team_id = str(idx)
        team_data = {}
        for team_key, team_value in zip(headers, row):
            team_data[team_key.strip()] = team_value.strip()
        json_data["nba_teams"][team_id] = team_data
    with open(file_path, mode="w", newline="") as file:
        json.dump(json_data, file, indent=4)


# CRUd functions + convert file type
raw_data = read_data(csv_input_path)
updated_data = update_data(copy.deepcopy(raw_data))
create_data(updated_data, csv_output_path)
map_to_json(updated_data, json_output_path)