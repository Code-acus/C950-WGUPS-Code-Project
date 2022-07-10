# Harrison Rogers, Student ID: 00632898
import csv
import datetime

from hashtable import HashTable
from package import Package

# class Main:
#     # This is the message the user will see displayed when the program starts
#     # The interface is accessible from here
#     def __init__(self):
#         main()
from truck import Truck

hash_map1 = HashTable()
# with open('./data/input_data.csv', encoding='utf-8-sig') as csv_file:
#     package_csv = csv.reader(csv_file, delimiter=',')
#     for row in package_csv:
#         package_id = row[0]
#         package_weight = row[1]
#         package_destination = row[2]
#         package = Package(package_id, package_weight, package_destination)
#         hash_map.package_insert(package)
#
#         first_truck_delivery = hash_map.package_search(package_id)
#         second_truck_delivery = hash_map.package_search(package_id)
#         final_truck_delivery = hash_map.package_search(package_id)

with open('./data/input_data.csv', encoding='utf-8-sig') as csv_file_1:
    read_in_csv = csv.reader(csv_file_1, delimiter=',')
    for row in read_in_csv:
        package_id = row[0]
        address = row[1]

        pkg = Package(package_id, address)

        # if package_id == '3':
        #     pkg.truck = 2
        #
        # if package_id == '6':
        #     pkg.truck = 3
        #
        # if package_id == '7':
        #     pkg.truck = 4

        hash_map1.package_insert(pkg)
    # print(hash_map1)

distance_table = [[]]
with open('./data/distance_data.csv') as csv_file_1:
    distance_csv = list(csv.reader(csv_file_1, delimiter=','))
    for row in distance_csv:
        distance_table.append(row)
print(distance_table)

address_dict = {}
with open('./data/distance_name_data.csv') as csv_file_2:
    distance_name_csv = list(csv.reader(csv_file_2, delimiter=','))
    for row in distance_name_csv:
        address_dict[row[0]] = row[1]
print(address_dict)

# TODO: Get the index for a given address
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


# TODO: Write the routine to deliver the packages for the trucks
def delivery_truck(truck):
    pass
    for package in truck.packages:
        package.truck = truck.truck_id
        package.delivery_date = datetime.datetime.now()
        package.delivery_mileage = get_mileage_for_address(package.address, truck.destination)
        package.delivery_status = "Delivered"
        hash_map1.package_insert(package)


def get_delivery_status(truck):
    package = hash_map1.package_find(package_id)
    if package is None:
        return "Package not found"
    else:
        return package.delivery_status


user_input = ''
while user_input != "3":
    # global convert_first_time, convert_second_time, first_time, second_time
    # Displays interface for users to select options for packages and trucks
    print("----------------------------------------------")
    print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
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
            for count in range(1, 41):
                try:
                    first_time = hash_map1.get_value(str(count))[9]
                    second_time = hash_map1.get_value(str(count))[10]
                    (hrs, mins, secs) = first_time.split(":")
                    convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    (hrs, mins, secs) = second_time.split(":")
                    convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                except ValueError:
                    pass

                # Determine which packages have left origin and are enroute to destination
                if convert_first_time >= convert_user_time:
                    hash_map1.get_value(str(count))[10] = "At origin"
                    hash_map1.get_value(str(count))[9] = "leaving origin at: " + first_time

                    # Print the current package details
                    print(f'Package ID: {hash_map1.get_value(str(count))[0]}, '
                          f'Package Delivery Status: {hash_map1.get_value(str(count))[10]}')

                # Determine which packages have left destination but have not yet been delivered
                elif convert_second_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        hash_map1.get_value(str(count))[10] = "In transit to destination"
                        hash_map1.get_value(str(count))[9] = "left destination at: " + first_time

                        # Print the current package details
                        print(f'Package ID: {hash_map1.get_value(str(count))[0]}, '
                              f'Package Delivery Status: {hash_map1.get_value(str(count))[10]}')


                # Determine which packages have been delivered
                else:
                    hash_map1.get_value(str(count))[10] = "Delivered at " + second_time
                    hash_map1.get_value(str(count))[9] = "Left at : " + first_time

                    # Print the current package details
                    print(f'Package ID: {hash_map1.get_value(str(count))[0]}, '
                          f'Package Delivery Status: {hash_map1.get_value(str(count))[10]}')

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
            count = input("Enter a package ID: ")
            first_time = hash_map1.get_value(str(count))[9]
            second_time = hash_map1.get_value(str(count))[10]
            input_time = input("Enter a time (HH:MM:SS): ")
            (hrs, mins, secs) = input_time.split(":")
            convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = first_time.split(":")
            convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = second_time.split(":")
            convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # Determine which packages have left origin and are enroute to destination
            if convert_first_time >= convert_user_time:
                hash_map1.get_value(str(count))[10] = "At origin"
                hash_map1.get_value(str(count))[9] = "leaving origin at: " + first_time

                # Print the current package details
                print(f'Package ID: {hash_map1.get_value(str(count))[0]}\n'
                      f'Street address: {hash_map1.get_value(str(count))[2]}\n'
                      f'Required delivery time: {hash_map1.get_value(str(count))[6]}\n'
                      f'Package weight: {hash_map1.get_value(str(count))[7]}\n'
                      f'Truck status: {hash_map1.get_value(str(count))[9]}\n'
                      f'Package delivery status: {hash_map1.get_value(str(count))[10]}\n')

            # Determine which packages have left destination but have not yet been delivered
            elif convert_second_time <= convert_user_time:
                if convert_user_time < convert_second_time:
                    hash_map1.get_value(str(count))[10] = "In transit to destination"
                    hash_map1.get_value(str(count))[9] = "left destination at: " + first_time

                    # Print the current package details
                    print(f'Package ID: {hash_map1.get_value(str(count))[0]}\n'
                          f'Street address: {hash_map1.get_value(str(count))[2]}\n'
                          f'Required delivery time: {hash_map1.get_value(str(count))[6]}\n'
                          f'Package weight: {hash_map1.get_value(str(count))[7]}\n'
                          f'Truck status: {hash_map1.get_value(str(count))[9]}\n'
                          f'Package delivery status: {hash_map1.get_value(str(count))[10]}\n')


            # Determine which packages have been delivered
            else:
                hash_map1.get_value(str(count))[10] = "Delivered at " + second_time
                hash_map1.get_value(str(count))[9] = "Left at : " + first_time

                # Print the current package details
                print(f'Package ID: {hash_map1.get_value(str(count))[0]}\n'
                      f'Street address: {hash_map1.get_value(str(count))[2]}\n'
                      f'Required delivery time: {hash_map1.get_value(str(count))[6]}\n'
                      f'Package weight: {hash_map1.get_value(str(count))[7]}\n'
                      f'Truck status: {hash_map1.get_value(str(count))[9]}\n'
                      f'Package delivery status: {hash_map1.get_value(str(count))[10]}\n')

        except ValueError:
            print('Invalid Entry')
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
