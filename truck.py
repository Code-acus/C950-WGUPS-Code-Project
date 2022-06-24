import csv
import datetime


class Truck:
    # Explain what the "with" does and why you are using this
    with open('./data/distance_data.csv') as csvfile1:
        distance_csv = list(csv.reader(csvfile1, delimiter=','))
    with open('./data/distance_name_data.csv') as csvfile2:
        distance_name_csv = list(csv.reader(csvfile2, delimiter=','))

    # Get the package address >>> runs as O(n)
    def get_package_address():
        return distance_name_csv
