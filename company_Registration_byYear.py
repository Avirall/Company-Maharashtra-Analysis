import csv
import matplotlib.pyplot as plt

# Function to process data and create the bar chart
def process_and_plot_registration_years(data_csv_path):
    with open(data_csv_path, newline='', encoding='ISO-8859-1') as csvfile:
        dataset = csv.DictReader(csvfile)
        val = []

        for row in dataset:
            row['DATE_OF_REGISTRATION'] = str(row['DATE_OF_REGISTRATION'])

            if len(row['DATE_OF_REGISTRATION']) == 10:
                val.append(row['DATE_OF_REGISTRATION'][:4])
            elif row['DATE_OF_REGISTRATION'][-2:] >= '00' and row['DATE_OF_REGISTRATION'][-2:] <= '20':
                row['DATE_OF_REGISTRATION'] = '20' + row['DATE_OF_REGISTRATION'][-2:]
                val.append(row['DATE_OF_REGISTRATION'])
            elif row['DATE_OF_REGISTRATION'] == 'NA':
                pass
            else:
                row['DATE_OF_REGISTRATION'] = '19' + row['DATE_OF_REGISTRATION'][-2:]
                val.append(row['DATE_OF_REGISTRATION'])

        year = {}

        for i in val:
            if i not in year:
                year[i] = 1
            else:
                year[i] += 1

        return year

# Function to create and display the bar chart
def plot_registration_years(year):
    year = dict(sorted(year.items()))
    plt.bar(year.keys(), year.values())
    plt.xticks(rotation=90)
    plt.show()

# Usage
data_csv_path = 'Dataset/Maharashtra.csv'
registration_years = process_and_plot_registration_years(data_csv_path)
plot_registration_years(registration_years)
