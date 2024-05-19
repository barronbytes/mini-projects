# BookBot: Problem Statement

The bookstore industry lacks an equivalent of the nutritional labels found on grocery items, presenting a lucrative business opportunity. With insight into the frequency of letters in text, parents and educators could optimize book selections for toddlers. Certain letters are easier or more challenging for young children to pronounce, making this information invaluable. Enter BookBot, a command-line tool designed to fulfill this market need by generating book reports with sorted letter frequency analysis.

## Getting Started

BookBot performs its analysis in Python. Ensure you have Python version 3.12.3 or greater installed on your Windows, Linux, or macOS system by downloading it from [here](https://www.python.org/downloads/). Download the files mentioned below and maintain the same project structure, with all files in the same folder. Ensure that the project folder contains a subfolder named **'books'** (lowercase), which includes the sample text files for analysis and testing.
- **main.py:** This code utilizes object-oriented programming principles and employs list comprehension for efficient data processing. Comments are provided throughout the codebase to enhance readability and explain the purpose of functions, along with their parameters and return data types.
- **test_main.py:** This file uses the **'unittest'** library for unit testing of functions. Comments are included for clarity. Edge casese that were considered included file not found and empty file scenarios.
- **.gitignore:** This file has been configured to exclude the contents of the books folder from git version control, as it contains data rather than code. Downloading this file is optional if this functionality for git is not needed.
- **books** folder**:** Include this as a subfolder. Save the included **.txt** text files. You can add new text files as well for future analysis and testing!

## Integrations

The project utilizes the **'string'** module for accessing the alphabet. It also employs the built-in **'unittest'** library for unit testing, which is similar to the **'JUnit'** library in Java. You can read more about the python testing library and its capabilities in the [official documentation](https://docs.python.org/3/library/unittest.html).

## Project Constraints

The project is limited to analyzing text files containing English-language content. It assumes that the text files provided are encoded using **UTF-8**. The tool currently operates solely within the command line interface, lacking a graphical user interface for broader accessibility.

## Improvements

The bullet points below will outline specific areas for improvement. These enhancements aim to make BookBot more robust, user-friendly, and versatile in future iterations.

- **User Interface:** The project currently operates solely within the command-line terminal. Introducing a web or mobile user interface would improve usability and accessibility.
- **API Integrations:** Using tools such as **Google Books API** would provide the ability to fetch a vast library of book content and metadeta directly, elmininating manual uploads and enhancing efficiency. The **AWS S3 API** can also be used to provide scalable, secure storage for book files, improving file management and retrieval.
- **Security:** The current process for using BookBot involves two manual steps: adding a **.txt** file to the books folder and entering the file path in the **'main.py'** file. Introducing a front-end component to BookBot would offer users added features like content uploading, but it would also introduce new security concerns to manage.
- **Data:** Using of a database would offer key benefits to the product. It would ensure structured data storage, maintaining integrity and consistency. Additionally, this would support complex querying for efficient data retrieval and analysis.
