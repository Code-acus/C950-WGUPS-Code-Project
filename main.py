# Harrison Rogers, Student ID: 00632898

import csv
import datetime
import package
from hashtable import HashTable
from package import Package
from truck import Truck

hash_map1 = HashTable()

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
        # print(row)

address_dict = {}
with open('./data/distance_name_data.csv') as csv_file_2:
    distance_name_csv = list(csv.reader(csv_file_2, delimiter=','))
    for row in distance_name_csv:
        address_dict[row[1]] = int(row[0])


# print(address_dict)

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
    while has_more_packages(truck):
        current_min_package = None
        current_min_dist = 100.0
        for package_id in truck.package_list:
            package = hash_map1.package_find(package_id)
            if package.is_not_delivered():

                package_loc_index = address_dict[package.address]
                # print(package_id, current_loc_index, package_loc_index)
                if current_loc_index > package_loc_index:
                    current_dist = float(distance_table[current_loc_index][package_loc_index])
                else:
                    current_dist = float(distance_table[package_loc_index][current_loc_index])
                    # Checking if current distance is less than min distance
                if current_dist < current_min_dist:
                    current_min_dist = current_dist
                    current_min_package = package

        if current_min_package is not None:
            mins = (current_min_dist * 60) / 18.0
            current_time = current_time + datetime.timedelta(minutes=mins)
            current_min_package.delivery_time = current_time
            current_loc_index = package_loc_index
            truck_distance += current_min_dist
            # print('**', current_loc_index, package_loc_index, truck.package_list.index(current_min_package.package_id))
            # my_test_local_var = truck.package_list.index(current_min_package.package_id)
            # truck.package_list.pop(my_test_local_var)
            print("Delivered package", current_min_package.package_id, "at", current_time, current_min_dist,
                  truck_distance)

        current_dist = float(distance_table[current_loc_index][0])
        truck_distance += current_dist
        truck.total_distance += truck_distance
        mins = (current_dist * 60) / 18.0
        current_time = current_time + datetime.timedelta(minutes=mins)
    print(truck.truck_id, "Delivered")
    return current_time


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


# Main run:

truck1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
truck2_list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
truck3_list = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

truck_1 = Truck(1, truck1_list, 18, datetime.datetime(2022, 1, 1, 8, 0, 0))
truck_2 = Truck(2, truck2_list, 18, datetime.datetime(2022, 1, 1, 9, 0, 5))
truck_3 = Truck(3, truck3_list, 18)

truck_1_finish_time = deliver_packages_for_truck(truck_1)
deliver_packages_for_truck(truck_2)
truck_3.start_time = truck_1_finish_time
deliver_packages_for_truck(truck_3)

user_input = ''
while user_input != "3":
    # global convert_first_time, convert_second_time, first_time, second_time
    # Displays interface for users to select options for packages and trucks
    print("----------------------------------------------")
    print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
    print("----------------------------------------------")
    print("Total Truck Distance:", truck_1.total_distance, truck_2.total_distance, truck_3.total_distance)
    print("----------------------------------------------")
    print("Please select from the options below:")
    print("1. Get status for all packages for a particular time frame")
    print("2. Get status single package for a particular time frame")
    print("3. Quit to exit the package query ")  # Get user input

    user_input = input("Enter your selection: ")

    # Case of user selects option 1
    # Get details for all packages at a particular time frame
    if user_input == "1":
        try:
            # Get the time frame from the user
            input_time = input("Enter a time (HH:MM:SS): ")
            (hrs, mins, secs) = input_time.split(":")
            convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # Complexity of this code is O(n^2)
            for package_id in range(1, 41):
                try:
                    first_time = hash_map1.get_value(str(package_id))  # [9]
                    second_time = hash_map1.get_value(str(package_id))  # [10]
                    (hrs, mins, secs) = first_time.split(":")
                    convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    (hrs, mins, secs) = second_time.split(":")
                    convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                except ValueError:
                    pass

                # Determine which packages have left origin and are enroute to destination
                if convert_first_time >= convert_user_time:
                    hash_map1.get_value(str(package_id))[10] = "At origin"
                    hash_map1.get_value(str(package_id))[9] = "leaving origin at: " + first_time

                    # Print the current package details
                    print(f'Package ID: {hash_map1.get_value(str(package_id))[0]}, '
                          f'Package Delivery Status: {hash_map1.get_value(str(package_id))[10]}')

                # Determine which packages have left destination but have not yet been delivered
                elif convert_second_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        hash_map1.get_value(str(package_id))[10] = "In transit to destination"
                        hash_map1.get_value(str(package_id))[9] = "left destination at: " + first_time

                        # Print the current package details
                        print(f'Package ID: {hash_map1.get_value(str(package_id))[0]}, '
                              f'Package Delivery Status: {hash_map1.get_value(str(package_id))[10]}')


                # Determine which packages have been delivered
                else:
                    hash_map1.get_value(str(package_id))[10] = "Delivered at " + second_time
                    hash_map1.get_value(str(package_id))[9] = "Left at : " + first_time

                    # Print the current package details
                    print(f'Package ID: {hash_map1.get_value(str(package_id))[0]}, '
                          f'Package Delivery Status: {hash_map1.get_value(str(package_id))[10]}')

        except IndexError:
            print(IndexError)
            exit()
        except ValueError:
            print('Invalid Entry')
            exit()


    # Case of user selects option 2
    # Get details for a single package at a particular time frame which should run in O(n)
    elif user_input == "2":
        try:
            # Get the time frame from the user
            package_id = input("Enter a package ID: ")
            input_time = input("Enter a time (HH:MM:SS): ")
            (hrs, mins, secs) = input_time.split(":")
            convert_user_time = datetime.datetime(2022, 1, 1, int(hrs), int(mins), int(secs))
            package_object = hash_map1.package_find(int(package_id))
            package_truck = get_truck_for_package_id(int(package_id))
            print(package_object.print_package_status_for_time(convert_user_time, package_truck.start_time))

        except ValueError as e:
            print('Invalid Entry', e)
            exit()

    # Case of user selects option 1
    # Option 1 will exit the program
    elif user_input == "1":
        exit()

    # Case Error
    # Case of user selects an invalid option
    else:
        print('Invalid Entry')
        exit()
