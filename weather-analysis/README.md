# EDA of Brazil Exporter Coffee Output vs Weather Trends [🏡](https://github.com/barronbytes/mini-projects/tree/main)

This mini-project allowed me to use pandas for **exploratory data analysis (EDA)** with the following scenario:

> You are a data engineer at a Brazil-based weather prediction startup called Curu-Sight. The goal of this startup is to analyze **weather trends** in Brazil and predict the **output** of non-durable consumer goods at harvest time.

> One major threat (barring tariffs) to Brazil's biggest export, coffee, is **leaf rust**. This fungus thrives in humid environments and causes plants to wither. Your company recently won a contract with the local government of Minas Gerais to analyze how humidity (and auxiliary measures) determine the yearly output of coffee.

> You will analyze a dataset that contains averages calculated based on rainfall, temperature, humidity, and wind metrics collected during the coffee growing season. You will also analyze a dataset that contains Minas Gerais' crop output. You will then combine these two datasets to explore how the weather influences coffee growth.

## Prerequisites [🔝](#eda-of-brazil-exporter-coffee-output-vs-weather-trends-)

Before running this project locally, ensure you ahve the following installed:

* IDE (VS Code, PyCharm, etc.)
* Instally Python 3.10+ version > for type hinting compatability
* Install pandas and matplotlib: `pip install pandas matplotlib`

## Lessons Learned [🔝](#eda-of-brazil-exporter-coffee-output-vs-weather-trends-)

I learned to do the following with CSV data:

* Concatenate datasets with identical columns > `explore_weather.ipynb` > create new CSV file > `data/weather/weather_data.csv`
* Merge datasets with different columns > `analysis.ipynb`
* Clean data > remove null value rows
* Filter data > select based upon criteria
* Use pandas for visualiztaions > line plots, histograms
* Calculate and interpret Pearson correlation coefficients

| Pearson Value(s) | Pearson Interpretation |
|:--------:|:--------------|
| 1 | Perfectly Positive |
| 0.7 | Strongly Positive |
| 0.4 | Moderately Positive |
| 0.1 | Weakly Positive
| 0 | None |
| -0.1 | Weakly Negative |
| -0.4 | Moderately Negative |
| -0.7 | Strongly Negative |
| -1 | Perfectly Negative | 

The following resources helped to use pandas in this project:

* [Pandas: Official API Reference](https://pandas.pydata.org/docs/reference/index.html)
* [Programiz: Introduction to Pandas](https://www.programiz.com/python-programming/pandas/introduction)
* [Medium: Part 6: (Combining DataFrames): Mastering Data Manipulation with Pandas](https://medium.com/mastering-the-art-of-data-science-a-comprehensive/part-6-combining-dataframes-mastering-data-manipulation-with-pandas-95a698c96ef8)

## Jupyter Notebooks [🔝](#eda-of-brazil-exporter-coffee-output-vs-weather-trends-)

There are three Jupyter notebooks with EDA findings:

* notebooks/explore_weather.ipynb
* notebooks/explore_coffee.ipynb
* notebooks/analysis.ipynb

## Datasets [🔝](#eda-of-brazil-exporter-coffee-output-vs-weather-trends-)

There are three CSV files:

* **data/weather/** > `weather_data1.csv`, `weather_data 2.csv`: This datset contains weather data from **January to May**.
* **data/crop/** > `coffee_output.csv`: This dataset contains coffee harvest data from **June to September**.

| Column | Weather Dataset |
|:---------|:--------------|
| year | Year of Harvest |
| rain_max | Average maximum (mm of rain)  |
| temp_avg | Average temperature (℃) |
| temp_max | Average maximum temperature (℃) |
| temp_min | Average minimum temperature (℃) |
| hum_max | Average maximum humidity (%) |
| hum_min | Average minimum humidity (%) |
| wind_max | Average maximum wind speed (m/s) |
| wind_avg | Average wind speed (m/s) |
| subdivision | Name of Brazilian sub-division |


| Column | Coffee Dataset |
|:---------|:--------------|
| country | Country of Harvest (Brazil) |
| subdivision | Name of Brazilian sub-division |
| type | Type of coffee bean |
| 60kgs_bag | 60 kg bags of coffee beans harvested (million bags) |
| year | Year of Harvest |
| nonbearing_trees | Amount of nonbearing coffee trees (million trees) |
| bearing_trees | Amount of bearing coffee trees (million trees) |
| nonbear_hectares | Hectares of nonbearing coffee trees (thousand hectares) |
| bearing_trees_per_hectare | Average number of bearing trees per hectare |
| nonbearing_trees_per_hectare | Average number of non-bearing trees per hectare |

## Credits & Contributions [🔝](#eda-of-brazil-exporter-coffee-output-vs-weather-trends-)

[The Knowledge House](https://www.theknowledgehouse.org/) provided the project requirements and raw data for this project. Contributions are welcome! Feel free to submit a pull request to improve the project or opena issue to report any problems.
