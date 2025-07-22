import os


class GetFileData():
    data_dir_name = "data"

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
    def get_data_files(root_dir:str) -> list[str]:
        '''
        Finds all files containing recorded heart rate measurements from experiment.

        Parameters:
            root_dir (str): Relative path for project directory.
        Returns:
            list(str): All data files from experiment.
        '''
        data_dir = os.path.join(root_dir, GetFileData.data_dir_name)
        dir_contents = os.listdir(data_dir)
        contents = [content for content in dir_contents if os.path.isfile(os.path.join(data_dir, content))]
        return sorted(contents)


    @staticmethod   
    def select_data_file(data_files: list[str]) -> int:
        '''
        Allows user to select data file for analysis.

        Parameters:
            data_files (list(str)): All data files from experiment.
        Returns:
            int: Index value for choosen data file. Will default to index 0 for invalid selection from user input.
        '''
        print("These files contain heart rate data:")
        options = "\n".join(f"[{i+1}] file=\"{file}\"" for i, file in enumerate(data_files))
        print(options)
        selection = input("\nEnter the file number you want to analyze.\nWill default to '1' for invalid input: ")
        indices = [str(n) for n in range(1, len(data_files)+1)]
        index = int(selection)-1 if selection in indices else 0
        return index


    @staticmethod
    def read_data(file_path: str) -> list[str]:
        '''
        Reads raw data for file user choose for analysis.

        Parameters:
            file_path (str): Path for file user choose for analysis.
        Returns:
            list(str): Raw data from file user choose for analysis.
        '''
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            raw_data = file.readlines()
        return raw_data


    @staticmethod
    def brain() -> list[str, list[str]]:
        '''
        Coordinates methods of class to allow user to choose file for analysis.

        Returns:
            list: Outputs file name and list of raw heart rate data user choose for analysis.
        '''
        root_dir = GetFileData.root_dir()
        is_data_dir_exists = os.path.isdir(os.path.join(root_dir, GetFileData.data_dir_name))
        data_files = GetFileData.get_data_files(root_dir) if is_data_dir_exists else []
        raw_data = []
        file_name = data_files[0]
        if data_files:
            file_index = GetFileData.select_data_file(data_files)
            file_name = data_files[file_index]
            file_path = os.path.join(root_dir, GetFileData.data_dir_name, file_name)
            file_lines = GetFileData.read_data(file_path)
            raw_data = file_lines
        return [file_name, raw_data]