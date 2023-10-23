import csv
import matplotlib.pyplot as plt

# Function to process data and create the bar chart
def process_and_plot_top_primary_activities_last_10_years(data_csv_path):
    val = {}

    with open(data_csv_path, newline='', encoding='ISO-8859-1') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            registration_date = row['DATE_OF_REGISTRATION']
            activity = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']

            if registration_date != 'NA':
                year = '20' + registration_date[-2:]

                if 2011 <= int(year) <= 2020:
                    if year not in val:
                        val[year] = {}

                    primary_activities = val[year]
                    primary_activities[activity] = primary_activities.get(activity, 0) + 1

    val = dict(sorted(val.items()))

    top_primary_activities = {}
    for year, activities in val.items():
        sorted_activities = dict(sorted(activities.items(), key=lambda item: item[1], reverse=True)[:5])
        top_primary_activities[year] = sorted_activities

    last_10_years = [year for year in top_primary_activities if 2011 <= int(year) <= 2020]
    activities_name = {key for inner_dict in top_primary_activities.values() for key in inner_dict.keys()}

    counts = []

    for activity in activities_name:
        counts_for_activity = [top_primary_activities[year].get(activity, 0) for year in last_10_years]
        if not all(count == 0 for count in counts_for_activity):
            counts.append(counts_for_activity)

    return last_10_years, activities_name, counts

# Function to create and display the bar chart
def plot_top_primary_activities_last_10_years(last_10_years, activities_name, counts):
    positions = list(range(len(last_10_years)))
    width = 0.1

    for i, activity_counts in enumerate(counts):
        positions = [(j + (width * i)) for j in positions]
        plt.bar(positions, activity_counts, width=width, label=activities_name.pop())

    plt.xlabel('Years')
    plt.ylabel('Activity Counts')
    plt.title('Top 5 Primary Activities Over the Last 10 Years (2011-2020)')
    plt.legend(title='Activities')
    plt.xticks(positions, last_10_years)
    plt.show()

# Usage
data_csv_path = 'Dataset/Maharashtra.csv'
last_10_years, activities_name, counts = process_and_plot_top_primary_activities_last_10_years(data_csv_path)
plot_top_primary_activities_last_10_years(last_10_years, activities_name, counts)
