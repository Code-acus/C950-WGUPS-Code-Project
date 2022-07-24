# Harrison Rogers, Student ID: 00632898

import csv
import datetime
from hashtable import HashTable
from package import Package
from truck import Truck

hash_map1 = HashTable()


def has_more_packages(truck):
    for package_id in truck.package_list:
        package = hash_map1.package_find(package_id)
        if package.is_not_delivered():
            return True
    return False


def deliver_packages_for_truck(truck):
    truck_distance = 0.0
    current_loc_index = 0
    current_time = truck.start_time
    print(truck.package_list)
    # Package delivery loop
    while has_more_packages(truck):
        current_min_package = None
        current_min_dist = 100.0
        for package_id in truck.package_list:
            package = hash_map1.package_find(package_id)
            if package.is_not_delivered():

                package_loc_index = address_dict[package.address]
                if current_loc_index > package_loc_index:
                    current_dist = float(distance_table[current_loc_index][package_loc_index])
                else:
                    current_dist = float(distance_table[package_loc_index][current_loc_index])
                if current_dist <= current_min_dist:
                    current_min_dist = current_dist
                    current_min_package = package

        mins = (current_min_dist * 60) / 18.0
        current_time = current_time + datetime.timedelta(minutes=mins)
        current_min_package.delivery_time = current_time
        current_min_package.mileage = current_min_dist
        current_loc_index = package_loc_index
        truck_distance += current_min_dist

    truck_distance += float(distance_table[current_loc_index][0])
    return current_time, truck_distance


def get_index_for_address(address):
    pass
    for address_entry in address_dict:
        if address == address_entry[2]:
            return int(address_entry[0])
    return -1


def get_mileage_for_address(starting_address, ending_address):
    start_index = get_index_for_address(starting_address)
    end_index = get_index_for_address(ending_address)

    if start_index != -1 and end_index != -1:
        if start_index > end_index:
            return float(distance_table[start_index][end_index])
        else:
            return float(distance_table[end_index][start_index])
    else:
        print("Bad address", starting_address, ending_address)
    return -1.0


def get_delivery_status(package_id):
    package = hash_map1.package_find(package_id)
    if package is None:
        return "Package not found"
    else:
        return package.delivery_status


def get_truck_for_package_id(package_id, truck_1=None, truck_2=None, truck_3=None):
    if package_id in truck_1.package_list:
        return truck_1
    if package_id in truck_2.package_list:
        return truck_2
    if package_id in truck_3.package_list:
        return truck_3


with open('./data/input_data.csv', encoding='utf-8-sig') as csv_file_1:
    read_in_csv = csv.reader(csv_file_1, delimiter=',')
    for row in read_in_csv:
        package_id = int(row[0])
        address = row[1]
        pkg = Package(package_id, address)
        hash_map1.package_insert(pkg)

distance_table = []
with open('./data/distance_data.csv') as csv_file_1:
    distance_csv = list(csv.reader(csv_file_1, delimiter=','))
    for row in distance_csv:
        distance_table.append(row)

address_dict = {}
with open('./data/distance_name_data.csv') as csv_file_2:
    distance_name_csv = list(csv.reader(csv_file_2, delimiter=','))
    for row in distance_name_csv:
        address_dict[row[1]] = int(row[0])

# Main run:
truck1_list = [1, 2, 3, 6, 7, 8, 10, 11, 12, 18, 21, 22, 23, 24, 25, 26]
truck2_list = [4, 5, 13, 14, 15, 16, 17, 19, 20, 27, 28, 29, 30]
truck3_list = [9, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

truck_1 = Truck(1, truck1_list, 18, datetime.datetime(2022, 1, 1, 8, 0, 0))
truck_2 = Truck(2, truck2_list, 18, datetime.datetime(2022, 1, 1, 9, 0, 5))
truck_3 = Truck(3, truck3_list, 18)

for package_id in truck_1.package_list:
    package = hash_map1.package_find(package_id)
    package.load_time = truck_1.start_time
truck_1.finish_time, truck_1.total_distance = deliver_packages_for_truck(truck_1)

for package_id in truck_2.package_list:
    package = hash_map1.package_find(package_id)
    package.load_time = truck_2.start_time
truck_2.finish_time, truck_2.total_distance = deliver_packages_for_truck(truck_2)

truck_3_delayed_start = datetime.datetime(2022, 1, 1, 10, 20, 0)
if truck_1.finish_time > truck_3_delayed_start:
    truck_3.start_time = truck_1.finish_time
else:
    truck_3.start_time = truck_3_delayed_start

print(truck_3.start_time)
for package_id in truck_3.package_list:
    package = hash_map1.package_find(package_id)
    package.load_time = truck_3.start_time
truck_3_finish_time, truck_3.total_distance = deliver_packages_for_truck(truck_3)

truck_total_miles = truck_1.total_distance + truck_2.total_distance + truck_3.total_distance
print("total_miles ", truck_total_miles)
user_input = ''
while user_input != "3":
    print("----------------------------------------------")
    print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
    print("----------------------------------------------")
    print("Total Truck Distance:", truck_total_miles)
    print("----------------------------------------------")
    print("Please select from the options below:")
    print("1. Get status for all packages for a particular time frame")
    print("2. Get status single package.")
    print("3. Quit to exit the package query ")  # Get user input

    user_input = input("Enter your selection: ")

    if user_input == "1":
        try:
            input_time = input("Enter a time (HH:MM:SS): ")
            (hrs, mins, secs) = input_time.split(":")
            convert_user_time = datetime.datetime(2022, 1, 1, int(hrs), int(mins), int(secs))

            # Complexity of this code is O(n^2)
            for package_id in range(1, 41):
                package = hash_map1.package_find(package_id)
                if package is not None:
                    truck = get_truck_for_package_id(package_id, truck_1, truck_2, truck_3)
                    print(package.print_package_status_for_time(convert_user_time, truck.start_time))

        except IndexError:
            print(IndexError)
            exit()


    # Get details for a single package at a particular time frame which should run in O(n)
    elif user_input == "2":
        try:
            package_id = input("Enter a package ID: ")
            package_object = hash_map1.package_find(int(package_id))
            if package_object is not None:
                print(package_object)

        except ValueError as e:
            print('Invalid Entry', e)
            exit()
