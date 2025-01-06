import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Clean the dataset: strip column names and drop missing values."""
    data.columns = data.columns.str.strip().str.replace('"', '')
    return data.dropna()

def filter_data(data, column, threshold):
    """Filter rows based on a column's threshold."""
    return data[data[column] > threshold]

def save_data(data, output_path):
    """Save the filtered dataset to a CSV file."""
    data.to_csv(output_path, index=False)

def plot_data(data, column, title, output_path):
    """Generate and save a bar plot for the top 10 cities."""
    plt.figure(figsize=(10, 6))
    plt.bar(data['City'].head(10), data[column].head(10), color='skyblue')
    plt.xticks(rotation=90)
    plt.title(title)
    plt.xlabel('City')
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    # Paths for input and output files
    air_input = r"../data/air_quality.csv"
    air_output = r"../output/high_air_pollution.csv"
    air_plot = r"../output/top_air_pollution.png"

    water_input = r"../data/water_pollution.csv"
    water_output = r"../output/high_water_pollution.csv"
    water_plot = r"../output/top_water_pollution.png"

    # Process air pollution data
    air_data = load_data(air_input)
    cleaned_air = clean_data(air_data)
    high_air = filter_data(cleaned_air, 'AirQuality', 30)
    save_data(high_air, air_output)
    plot_data(high_air, 'AirQuality', 'Top 10 Cities with High Air Pollution', air_plot)

    # Process water pollution data
    water_data = load_data(water_input)
    cleaned_water = clean_data(water_data)
    high_water = filter_data(cleaned_water, 'WaterPollution', 30)
    save_data(high_water, water_output)
    plot_data(high_water, 'WaterPollution', 'Top 10 Cities with High Water Pollution', water_plot)
