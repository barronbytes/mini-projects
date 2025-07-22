from etl_extract import Extract
from etl_transform import Transform
from etl_load import Load
from control import Control


def main():
    run_all = True
    while run_all:
        is_extracted, file_name, reviews = Extract.brain()
        data_labels, sentiments = Transform.brain(reviews) if is_extracted else ([], {})
        data_counts = [sentiments[label] for label in data_labels]
        Load.create_bar_graph(file_name, data_labels, data_counts)
        run_all = Control.clear_screen() if is_extracted else False


if __name__ == "__main__":
    main()
