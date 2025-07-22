# File Handling [🏡](https://github.com/barronbytes/mini-projects/tree/main)

Data can be stored in different formats, and this mini-project demonstrates how to read, write, and convert between them. The project files use the modules `os`, `csv`, `json`, and `copy` to handle CRUD operations.

## Prerequisites [🔝](#file-handling-)

Before running this project locally, ensure you have the following installed:

* IDE (VS Code, PyCharm, etc.)
* Install Python 3.10+ version > for type hinting compatability

## Lessons Learned [🔝](#file-handling-)

The **src** folder contains files that modify data saved inside subfolders.

**nba.py:** This file reads CSV data, updates CSV data, and converts to JSON data. Relevant methods:
* **create_data():** Write file with `csv.writer()` and `writer.writerows()` methods.
* **read_data():** Read file with `csv.reader()` method.
* **update_data():** Create `deep copy` of orignal data to update.
* **map_to_json():** Uses `json.dump()` method for JSON data conversion.

**pokemon.py:** This file reads JSON data, updates JSON data, and converts to CSV data. Relevant methods:
* **create_data():** Write file with `json.dump()` method.
* **read_data():** Read file with `json.load()` method.
* **update_data():** Create `deep copy` of orignal data to update.
* **map_to_csv():** Uses `csv.DictWriter()`, `writer.writeheader()`, and `writer.writerows()` methods for CSV data conversion.

## Credits [🔝](#file-handling-)

The following resources helped me learn about the `csv` and `json` modules:
* [CSV Documentation](https://docs.python.org/3/library/csv.html): Developer documentation for method arguments and return values.
* [JSON Documentation](https://docs.python.org/3/library/json.html): Developer documentation for method arguments and return values.