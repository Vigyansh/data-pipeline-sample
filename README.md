# data-pipeline-sample
Environmental Data Pipeline

Overview

The Environmental Data Pipeline processes and analyzes air quality and water pollution data to identify cities with high pollution levels. The goal is to provide actionable insights and visualize the data for informed decision-making.


Key Features:

Data Cleaning: Removes missing or invalid data for better accuracy.

Threshold-Based Filtering:
Air Quality > 30.
Water Pollution > 30.

Insights Generation: Highlights cities with the highest pollution levels.

Data Visualization: Bar charts showcasing top polluted cities.

Outputs: Saves cleaned and filtered data for future use.

Process Workflow
Step 1: Data Extraction
The pipeline processes raw datasets for air quality and water pollution.
Step 2: Data Transformation
Cleans the data by removing missing values and standardizing column names.
Filters cities based on:
High air pollution (Air Quality > 30).
High water pollution (Water Pollution > 30).
Step 3: Data Output
Generates filtered datasets:
high_air_pollution.csv
high_water_pollution.csv

Insights:
Air Pollution:
Total Cities with High Air Pollution: 3187.
City with the Worst Air Pollution: Vaduz (100).
Water Pollution:
Total Cities with High Water Pollution: 2833.
City with the Worst Water Pollution: Nowy Sacz (100).

Visualizations
The pipeline generates bar charts for the top 10 polluted cities:

High Air Pollution Levels by City

High Water Pollution Levels by City


Files

Input:
Raw datasets for air quality and water pollution.

Output:
Filtered Data:
output/high_air_pollution.csv
output/high_water_pollution.csv

Visualizations:
output/top_air_pollution.png
output/top_water_pollution.png

How to Run:

Prerequisites:
Python 3.x installed on your machine.

Dependencies:
Install the required libraries using the `requirements.txt` file:
pip install -r requirements.txt

Steps:
Clone the repository:
git clone https://github.com/Vigyansh/data-pipeline-sample.git
cd data-pipeline-sample
Place raw datasets in the data/ folder.
Run the pipeline:
python src/etl_pipeline.py
Check the output/ folder for the results.

Future Enhancements:

Add support for additional pollution metrics.
Automate data ingestion and pipeline execution.
Implement interactive dashboards using Tableau or Power BI.