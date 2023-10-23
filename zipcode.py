import csv
import matplotlib.pyplot as plt

# Function to process data and create the bar chart
def process_and_plot_district_count(data_csv_path, pincode_csv_path):
    zipcodes = []
    district_count = {}
    district_name = {}

    with open(data_csv_path, newline='', encoding='ISO-8859-1') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            row['DATE_OF_REGISTRATION'] = str(row['DATE_OF_REGISTRATION'])
            if row['DATE_OF_REGISTRATION'][-2:] == '15' and row['Registered_Office_Address'][-6:] != '000000':
                val = row['Registered_Office_Address'][-6:]
                zipcodes.append(val)

    with open(pincode_csv_path, newline='', encoding='ISO-8859-1') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            district_name[row['Pin Code']] = row['District']
            district_count[row['District']] = 0

    for i in zipcodes:
        if i in district_name.keys():
            district_count[district_name[i]] += 1

    return district_count

# Function to create and display the bar chart
def plot_district_count(district_count):
    plt.bar(district_count.keys(), district_count.values())
    plt.show()

# Usage
data_csv_path = 'Dataset/Maharashtra.csv'
pincode_csv_path = 'Dataset/pincode.csv'
district_count = process_and_plot_district_count(data_csv_path, pincode_csv_path)
plot_district_count(district_count)
