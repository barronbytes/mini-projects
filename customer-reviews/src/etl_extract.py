import os
import json


class Extract():
    data_dir_name = "data"
    data_file_extension = ".json"
    data_file_dict_key = "results"


    @staticmethod
    def root_dir() -> str:
        '''
        Finds relative path for directory one level below current file directory.

        Returns:
            str: Relative path for project directory.
        '''
        file_path = os.path.relpath(__file__)
        file_dir = os.path.dirname(file_path)
        root_dir = os.path.relpath(os.path.join(file_dir, ".."))
        return root_dir


    @staticmethod
    def get_data_files(root_dir: str) -> list[str]:
        '''
        Finds all JSON files contianing raw sentiment review data.

        Parameters:
            root_dir (str): Relative path for project directory.
        Returns:
            list (str): All JSON files from `data` folder.
        '''
        data_dir = os.path.join(root_dir, Extract.data_dir_name)
        contents = os.listdir(data_dir)
        files = [
            content
            for content in contents
            if os.path.isfile(os.path.join(data_dir, content)) and content.endswith(Extract.data_file_extension)
        ]
        return sorted(files)


    @staticmethod
    def select_data_file(data_files: list[str]) -> int:
        '''
        Allow users to select JSON file for analysis, and determines its index value from options.

        Parameters:
            data_files (list(str)): All JSON files from `data` folder.
        Returns:
            int: Index value for choosen data file. Will default to 0 for invalid selection from user input.
        '''
        print("These files contain raw sentiment review data from surveys.")
        options = "\n".join(f"[{i}] file = \"{file}\"" for i, file in enumerate(data_files, start=1))
        print(options)
        selection = input("\nEnter a file number to analyze.\nWill default to '1' for invalid input: ")
        indices = [str(n) for n in range(1, len(data_files)+1)]
        index = int(selection)-1 if selection in indices else 0
        return index


    @staticmethod
    def read_data(file_path: str) -> list[str]:
        '''
        Reads raw JSON data for file user choose for analysis.

        Parameters:
            file_path (str): Path file.
        Returns:
            list (str): Customer product reviews.
        '''
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            reviews = json.load(file)
        return reviews[Extract.data_file_dict_key]


    @staticmethod
    def brain() -> tuple[bool, str, list[str]]:
        '''
        Coordinates class methods to complete extraction step of ETL pipeline. Edge cases considered:
        (1) is_data_dir_exists: `data` directory doesn't exist
        (2) data_files: `data` directory has no JSON file
        (3) file_index: user chooses invalid index range number

        Edge cases not considered:
        (1) JSON file is empty
        (2) JSON file is not in dictionary format
        (3) JSON file is missing "results" key

        Returns:
            tuple: Uses truthy/falsy value of data_files to determine output:
                - If False -> (False, "", [])
                - If True -> (True, str of file_name, []) or (True, str of file_name, list[str of reviews])
        '''
        root_dir = Extract.root_dir()
        is_data_dir_exists = os.path.isdir(os.path.join(root_dir, Extract.data_dir_name))
        data_files = Extract.get_data_files(root_dir) if is_data_dir_exists else []
        file_name = ""
        file_path = ""
        if data_files:
            file_index = Extract.select_data_file(data_files)
            file_name = data_files[file_index]
            file_path = os.path.join(root_dir, Extract.data_dir_name, file_name)
        else:
            error_not_found = input("Error: Data file not found. Press 'enter' to exit program.")
        reviews = Extract.read_data(file_path) if file_path else []
        return (bool(data_files), file_name, reviews)
