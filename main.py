##

# Harrison Rogers, Student ID: 00632898

from datetime import datetime
from package import get_hash_map


class Main:
    # global convert_first_time, convert_second_time, first_time, second_time
    print("----------------------------------------------")
    print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
    print("----------------------------------------------")

    user_input = input("Please select from the options below:"
                       "1. Get status for all packages for a particular time frame"
                       "2. Get status single package for a particular time frame"
                       "3. Quit to exit the package query ")  # Get user input

    while user_input is not "3. Quit to exit the package query":
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
                        first_time = get_hash_map().get_value(str(count))[9]
                        second_time = get_hash_map().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(":")
                        convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = second_time.split(":")
                        convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    # Determine which packages have left origin and are enroute to destination
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get_value(str(count))[10] = "At origin"
                        get_hash_map().get_value(str(count))[9] = "leaving origin at: " + first_time

                        # Print the current package details
                        print(f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                              f'Package Delivery Status: {get_hash_map().get_value(str(count))[10]}')

                    # Determine which packages have left destination but have not yet been delivered
                    elif convert_second_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count))[10] = "In transit to destination"
                            get_hash_map().get_value(str(count))[9] = "left destination at: " + first_time

                            # Print the current package details
                            print(f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                  f'Package Delivery Status: {get_hash_map().get_value(str(count))[10]}')


                    # Determine which packages have been delivered
                    else:
                        get_hash_map().get_value(str(count))[10] = "Delivered at " + second_time
                        get_hash_map().get_value(str(count))[9] = "Left at : " + first_time

                        # Print the current package details
                        print(f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                              f'Package Delivery Status: {get_hash_map().get_value(str(count))[10]}')

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
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                input_time = input("Enter a time (HH:MM:SS): ")
                (hrs, mins, secs) = input_time.split(":")
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = first_time.split(":")
                convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = second_time.split(":")
                convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Determine which packages have left origin and are enroute to destination
                if convert_first_time >= convert_user_time:
                    get_hash_map().get_value(str(count))[10] = "At origin"
                    get_hash_map().get_value(str(count))[9] = "leaving origin at: " + first_time

                    # Print the current package details
                    print(f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                          f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                          f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                          f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                          f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                          f'Package delivery status: {get_hash_map().get_value(str(count))[10]}\n')

                # Determine which packages have left destination but have not yet been delivered
                elif convert_second_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        get_hash_map().get_value(str(count))[10] = "In transit to destination"
                        get_hash_map().get_value(str(count))[9] = "left destination at: " + first_time

                        # Print the current package details
                        print(f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                              f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                              f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                              f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                              f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                              f'Package delivery status: {get_hash_map().get_value(str(count))[10]}\n')


                # Determine which packages have been delivered
                else:
                    get_hash_map().get_value(str(count))[10] = "Delivered at " + second_time
                    get_hash_map().get_value(str(count))[9] = "Left at : " + first_time

                    # Print the current package details
                    print(f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                          f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                          f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                          f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                          f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                          f'Package delivery status: {get_hash_map().get_value(str(count))[10]}\n')

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


class Main:
    # This is the message the user will see displayed when the program starts
    # The interface is accessible from here
    def __init__(self):
        main()
