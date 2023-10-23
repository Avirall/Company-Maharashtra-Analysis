import csv
import matplotlib.pyplot as plt

# Function to process data and create the histogram
def process_and_plot_authorized_cap_distribution(data_csv_path):
    with open(data_csv_path, newline='', encoding='ISO-8859-1') as csvfile:
        dataset = csv.DictReader(csvfile)

        authorized_cap_bin = {
            '<=1Lakh': 0,
            '1 to 10 lakh': 0,
            '10 lakh to 1 Crore': 0,
            '1crore to 10 crore': 0,
            '>10 crore': 0
        }

        for row in dataset:
            val = float(row['AUTHORIZED_CAP'])
            if val <= 100000:
                authorized_cap_bin['<=1Lakh'] += 1
            elif 100000 < val <= 1000000:
                authorized_cap_bin['1 to 10 lakh'] += 1
            elif 1000000 < val <= 10000000:
                authorized_cap_bin['10 lakh to 1 Crore'] += 1
            elif 10000000 < val <= 100000000:
                authorized_cap_bin['1crore to 10 crore'] += 1
            else:
                authorized_cap_bin['>10 crore'] += 1

    return authorized_cap_bin

# Function to create and display the histogram
def plot_authorized_cap_distribution(authorized_cap_bin):
    plt.hist(authorized_cap_bin.keys(), bins=5, weights=authorized_cap_bin.values(), edgecolor='black')
    plt.show()

# Usage
data_csv_path = 'Dataset/Maharashtra.csv'
authorized_cap_bin = process_and_plot_authorized_cap_distribution(data_csv_path)
plot_authorized_cap_distribution(authorized_cap_bin)
