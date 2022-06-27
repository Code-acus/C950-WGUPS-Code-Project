from typing import List, Union, Any

from hashmap import HashTable
import csv

# read in the csv file
with open('./data/distance_data.csv') as csvfile1:
    read_in_csv = list(csv.reader(csvfile1, delimiter=','))

    # Creates an instance of the HashTable class
    hash_map = HashTable(len(read_in_csv))
    # First Truck Delivery
    first_truck_delivery: List[List[Union[str, Any]]] = []
    # Second Truck Delivery
    second_truck_delivery = []
    # Last Truck Delivery
    last_truck_delivery = []

    # Inserts the data into the hash table with key/value pairs should run in O(n)
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

        value = [package_id, address, city, state, zip_code, delivery_time, size, notes, delivery_start_time,
                 address_location, delivery_status]

        # Conditional statement to determine which truck should be assigned to the package
        # The packages then will be dropped into a nested list

        # Correct incorrect package details
        if "84104" in value[5] and '10:30:00' not in value[6]:
            delivery_time.append(value)

        # First Truck Delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck_delivery.append(value)

        # Second Truck Delivery
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            second_truck_delivery.append(value)

        # Check remaining packages
        if value not in first_truck_delivery and value not in second_truck_delivery and value \
                not in last_truck_delivery:
            second_truck_delivery.append(value) if len(second_truck_delivery) < len(
                first_truck_delivery) else last_truck_delivery.append(value)

        # Inserts the data into the hash table
        hash_map.insert(package_id, value)

    # Get packages on the delivery route - should run in O(1)
    def get_first_delivery():
        return first_truck_delivery

    # Get packages on the delivery route - should run in O(1)
    def get_second_delivery():
        return first_truck_delivery

    # Get packages on the delivery route - should run in O(1)
    def get_last_delivery():
        return last_truck_delivery

    # Get full list of packages - should run in O(1)
    def get_hash_map():
        return hash_map
