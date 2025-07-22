from get_file_data import GetFileData
from cleaner import Cleaner
from metrics import Metrics
from visualize import Visualize


def main():
    '''
    Main function that coordinates actions of entire project files as follows:
    (1) Allow user to choose data for analysis via GetFileData class
    (2) Clean data via Cleaner class
    (3) Calculcate summary statistics via Metrics class, and displays results via print_results() method
    (4) Generate visualizations of data via Visualize class
    '''
    file_name, raw_data = GetFileData.brain()
    clean_data = Cleaner(raw_data).brain()
    stats = Metrics().brain(clean_data) if isinstance(clean_data, list) and len(clean_data) >= 1 else [0, 0, 0]
    Metrics().print_results(stats)
    Visualize.brain(file=file_name, data=clean_data)


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()