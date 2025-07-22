class Cleaner():
    
    def __init__(self, data: list[str]):
        '''
        Initializes a Cleaner instance.

        Parameters:
            data (list[str]): Raw data values for heart rate measurements.
        '''
        self.data = data


    # object string representation        
    def __repr__(self) -> str:
        return f"Cleaner(data={self.data})"


    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, Cleaner):
            equality = self.data == other.data
        return equality


    def is_list(self) -> bool:
        '''
        Determines if raw data input is of type Boolean.

        Returns:
            bool: True if class initialized with list; otherwise, False.
        '''
        return isinstance(self.data, list)


    @staticmethod
    def clean_data(data: list[str]) -> list[int] | None:
        '''
        Cleans raw data input used to initialize class.

        Parameters:
            data (list[str]): Raw data values for heart rate measurements.
        Returns:
            list[int] | None: Clean data of heart rates if class initialized with list of numbers; otherwise, None. 
        '''
        data_strings = [d.strip() for d in data if isinstance(d, str)]
        data_numbers = [int(d) for d in data_strings if d.isdigit()]
        return data_numbers if data_numbers else None


    def brain(self) -> list[int] | None:
        '''
        Coordinates methods of class to clean raw data used to initialize class; returns None for invalid input.

        Returns:
            list[int] | None: Clean data of heart rates if class initialized with list of numbers; otherwise, None. 
        '''
        is_list = self.is_list()
        clean_data = Cleaner.clean_data(self.data) if is_list else None
        return clean_data