import matplotlib.pyplot as plt
import numpy as np
import os
import shutil


class Visualize():

    dst_dir_name = "images"

    @staticmethod
    def line_plot(file: str, data: list[int], dst_path: str) -> None:
        '''
        Creates line plot visualization.

        Parameters:
            file (str): File name.
            data (list[int]): Clean data of heart rate numbers.
            dst_path (str): Destination path for saving visualization images.
        '''
        # set data
        time_increment = 5
        time = time_increment*len(data)
        x = np.arange(0.0, time, time_increment)
        y = data

        # plot data
        figure, axes = plt.subplots()
        axes.plot(x, y)

        # label data
        axes.set(xlabel="Time (minutes)", ylabel="Heart Rate (bpm)", title=f"Heart Rate Data for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(dst_path, f"{file_name}_line_plot.png"))


    @staticmethod
    def box_plot(file: str, data: list[int], dst_path: str) -> None:
        '''
        Creates box plot visualization.

        Parameters:
            file (str): File name.
            data (list[int]): Clean data of heart rate numbers.
            dst_path (str): Destination path for saving visualization images.
        '''
        # plot data
        figure, axes = plt.subplots()
        axes.boxplot(data, vert=False)  # Set vertical=False for horizontal box plot

        # label data
        axes.set(xlabel="Heart Rate (bpm)", ylabel="Study Participant", title=f"Heart Rate Box Plot for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(dst_path, f"{file_name}_box_plot.png"))


    @staticmethod
    def histogram(file: str, data: list[int], dst_path: str) -> None:
        '''
        Creates histogram visualization.

        Parameters:
            file (str): File name.
            data (list[int]): Clean data of heart rate numbers.
            dst_path (str): Destination path for saving visualization images.
        '''
        # set data
        bins = 10

        # plot data
        figure, axes = plt.subplots()
        axes.hist(data, bins=bins, edgecolor="black")

        # label data
        axes.set(xlabel="Heart Rate (bpm)", ylabel="Frequency", title=f"Heart Rate Histogram for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(dst_path, f"{file_name}_histogram.png"))


    @staticmethod
    def create_and_wipe_directory() -> str:
        '''
        Ensures clean destination directory exists and returns destination path.

        Returns:
            str: Destination path for saving visualization images.
        '''
        dst_path = os.path.join(os.path.dirname(__file__), "..", Visualize.dst_dir_name)
        os.makedirs(dst_path, exist_ok=True)
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        os.mkdir(dst_path)
        return dst_path


    @staticmethod
    def brain(file: str, data: list[int]) -> None:
        '''
        Coordinates methods of class to save visualization images in destination directory.

        Parameters:
            file (str): File name.
            data (list[int]): Clean data of heart rate numbers.
        '''
        dst_path = Visualize.create_and_wipe_directory()

        Visualize.box_plot(file, data, dst_path)
        Visualize.line_plot(file, data, dst_path)
        Visualize.histogram(file, data, dst_path)