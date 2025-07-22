# Requests Module with GoREST API [🏡](https://github.com/barronbytes/mini-projects/tree/main)

This mini-project allowed me to practice using Python’s `requests` module to perform basic CRUD operations on a RESTful API.

* The open-source [GoREST API](https://gorest.co.in/) was used to interact with data.
* API endpoints were explored and tested with [postman](https://www.postman.com/) before implementing code.

## Prerequisites

Before running this project locally, ensure you have the following installed:

* IDE (VS Code, PyCharm, etc.)
* Install Python 3.10+ version > for type hinting compatability
* Install requests module: `python3 -m pip install requests`

## Lessons Learned

The following modules from the `requests` module perform CRUD operations:

* **Create**: `r = requests.post(url, headers, data)`
* **Read**: `r = requests.get(url)`, `data = r.json()`
* **Update**: `r = requests.put(url, headers, data)`
* **Delete**: `r = requests.delete(url, headers)`

The following best practices were used:

* **config.py**: Prevented API key exposure via **environmental variable** use.
* **get.py**: Used try-catch block to handle `get()` method errors.

## Credits

The following resources helped me learn about the `requests` module:
* [StatLearn Tech](https://www.youtube.com/watch?v=05sP5ST4Bus&list=PLll2u-uqtmZOkjgSczFw1CwnxV3Dw6sEF): YouTube playlist used for guidance.
* [Requests Documentation](https://requests.readthedocs.io/en/latest/api/): Developer documentation for method arguments and return values.