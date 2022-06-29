import csv
import datetime
import csv_reader

# This code creates the needed empty lists to store the data
import distance as distance

first_delivery = []
second_delivery = []
third_delivery = []
distances_of_first_truck = []
distances_of_second_truck = []
distances_of_third_truck = []

# Truck departure times from hub
first_truck_departure_times = ['08:00:00']
second_truck_departure_times = ['09:10:00']
third_truck_departure_times = ['11:00:00']

# Set the delivery start time to that of the first leave time for the packages assigned to the first truck
for index, value in enumerate(csv_reader.get_first_truck_delivery()):
    csv_reader.get_first_truck_delivery()[index][9] = first_truck_departure_times[0]
    first_delivery.append(csv_reader.get_first_truck_delivery()[index])

# Compare the addresses of the first truck to the address list which should run O(n^2)
for index, outer in enumerate(csv_reader.first_delivery()):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            distances_of_first_truck.append(outer[0])
            first_delivery[index][1] = inner[0]

# Make a ccall to the Algorithm to get packages for the first truck
distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# Calculate the total distance of the first truck and the distance of each package which should run in O(n)
for index in range(len(distance.first_truck_index())):
    try:
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]),
                                                 int(distance.first_truck_index()[index + 1]), total_distance_1)
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]),
                                                                          int(distance.first_truck_index()[index + 1])),
                                            first_truck_departure_times)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_table().update(int(distance.first_truck_list()[index][0], first_delivery))

    except IndexError:
        pass

        # Set delivery start to second truck departure time for all second truck packages which should run in O(n)
    for index, value in enumerate(csv_reader.get_second_truck_delivery()):
        csv_reader.get_second_truck_delivery()[index][9] = second_truck_departure_times[0]
        second_delivery.append(csv_reader.get_second_truck_delivery()[index])

    # Compare the addresses of the second truck to the address list which should run O(n^2)
    for index, outer in enumerate(second_delivery()):
        for inner in distance.get_address():
            if outer[2] == inner[2]:
                distances_of_second_truck.append(outer[0])
                second_delivery[index][1] = inner[0]

    # Call Algorithm to sort packages for the second truck
    distance.get_shortest_route(second_delivery, 2, 0)
    total_distance_2 = 0

    # Calculate the total distance of the second truck and the distance of each package which should run in O(n)
    for index in range(len(distance.second_truck_index())):
        try:
            total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]),
                                                     int(distance.second_truck_index()[index + 1]), total_distance_2)
            deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]),
                                                                              int(distance.second_truck_index()[
                                                                                      index + 1])),
                                                second_truck_departure_times)
            distance.second_truck_list()[index][10] = (str(deliver_package))
            csv_reader.get_hash_table().update(int(distance.second_truck_list()[index][0], second_delivery))

        except IndexError:
            pass
