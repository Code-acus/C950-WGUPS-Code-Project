from typing import List, Union, Any
from hashtable import HashTable
import csv


class Package:
    def __init__(self, package_id, package_weight, package_destination):
        self.package_id = package_id
        self.package_weight = package_weight
        self.package_destination = package_destination

    def get_package_id(self):
        return self.package_id

    def get_package_weight(self):
        return self.package_weight

    def get_package_destination(self):
        return self.package_destination


# read in the csv files and create a hash table
# Process package file first similar to line 27 - test hash table with something to put it in - process package file

hash_map = HashTable()

with open('./data/input_data.csv', encoding='utf-8-sig') as csv_file:
    package_csv = csv.reader(csv_file, delimiter=',')
    for row in package_csv:
        package_id = row[0]
        package_weight = row[1]
        package_destination = row[2]
        package = Package(package_id, package_weight, package_destination)
        hash_map.package_insert(package)

        first_truck_delivery = hash_map.package_search(package_id)
        second_truck_delivery = hash_map.package_search(package_id)
        final_truck_delivery = hash_map.package_search(package_id)

with open('./data/distance_data.csv', encoding='utf-8-sig') as csv_file_1:
    read_in_csv = csv.reader(csv_file_1, delimiter=',')
    for row in read_in_csv:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        delivery_time = row[5]
        size = row[6]
        notes = row[7]

        delivery_start_time = ' '
        address_location = ' '
        delivery_status = ' '

        first_truck_delivery = []
        second_truck_delivery = []
        final_truck_delivery = []
        value = [package_id, address, city, state, zip_code, delivery_time, size, notes, delivery_start_time,
                 address_location, delivery_status]

        # Conditional statement to determine which truck should be assigned to the package
        # The packages then will be dropped into a nested list

        # Correct incorrect package details
        if "84104" in value[5] and '10:30:00' not in value[6]:
            delivery_time.join(value)

        # First Truck Delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck_delivery.append(value)

        # Second Truck Delivery
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            second_truck_delivery.append(value)

        # Check remaining packages
        if value not in first_truck_delivery and value not in second_truck_delivery and value \
                not in final_truck_delivery:
            second_truck_delivery.append(value) if len(second_truck_delivery) < len(
                first_truck_delivery) else final_truck_delivery.append(value)

        # Inserts the data into the hash table
        hash_map.insert(package_id, value)


# Get packages on the delivery route runs in O(1) time
def get_first_truck_delivery():
    return first_truck_delivery


# Get packages on the delivery route runs in O(1) time
def get_second_truck_delivery():
    return first_truck_delivery


# Get packages on the delivery route runs in O(1) time
def get_final_truck_delivery():
    return final_truck_delivery


# Get full list of packages runs in O(1) time
def get_hash_map():
    return hash_map


# Get the current package distance runs in O(1) time
def get_hash_table():
    return None
