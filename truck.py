#

import distance
import package

class Truck:
    def __init__(self, truck_id, truck_capacity, truck_speed):
        self.truck_id = truck_id
        self.truck_capacity = truck_capacity
        self.truck_speed = truck_speed
        self.packages = []
        self.packages_indices = []
        self.packages_indices.append('0')
        self.packages_indices_2 = []
        self.packages_indices_2.append('0')
        self.packages_indices_3 = []
        self.packages_indices_3.append('0')
        self.packages_indices_4 = []
        self.packages_indices_4.append('0')
        self.packages_indices_5 = []
        self.packages_indices_5.append('0')
        self.packages_indices_6 = []
        self.packages_indices_6.append('0')
        self.packages_indices_7 = []
        self.packages_indices_7.append('0')
        self.packages_indices_8 = []
        self.packages_indices_8.append('0')
        self.packages_indices_9 = []
        self.packages_indices_9.append('0')
        self.packages_indices_10 = []
        self.packages_indices_10.append('0')
        self.packages_indices_11 = []
        self.packages_indices_11.append('0')
        self.packages_indices_12 = []
        self.packages_indices_12.append('0')
        self.packages_indices_13 = []
        self.packages_indices_13.append('0')
        self.packages_indices_14 = []
        self.packages_indices_14.append('0')
        self.packages_indices_15 = []
        self.packages_indices_15.append('0')
        self.packages_indices_16 = []
        self.packages_indices_16.append('0')
        self.packages_ind
# Empty lists created to store the addresses of the trucks
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []

# Times the trucks leave the hub
first_leave_times = ['8:00:00']
second_leave_times = ['9:10:00']
third_leave_times = ['11:00:00']

# Set delivery_start to first_leave_time for all truck one packages -> O(n)
for index, value in enumerate(package.get_first_truck_delivery()):
    package.get_first_truck_delivery()[index][9] = first_leave_times[0]
    first_delivery.append(package.get_first_truck_delivery()[index])

# Compare truck one addresses to address list -> O(n^2)
for index, outer in enumerate(first_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_truck_distances.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm to sort packages for first truck
distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# Calculate total distance of the first truck and distance of each package -> O(n)
for index in range(len(distance.first_truck_index())):
    try:
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]),
                                                 int(distance.first_truck_index()[index + 1]), total_distance_1)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]),
                                                                          int(distance.first_truck_index()[index + 1])),
                                            first_leave_times)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        package.get_hash_map().update(int(distance.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# Set delivery_start to second_leave_time for all truck two packages -> O(n)
for index, value in enumerate(package.get_second_truck_delivery()):
    package.get_second_truck_delivery()[index][9] = second_leave_times[0]
    second_delivery.append(package.get_second_truck_delivery()[index])

# Compare truck two addresses to address list -> O(n^2)
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            second_truck_distances.append(outer[0])
            second_delivery[index][1] = inner[0]

# Call algorithm to sort packages for second truck
distance.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0

# Calculate total distance of the second truck and distance of each package -> O(n)
for index in range(len(distance.second_truck_index())):
    try:
        total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]),
                                                 int(distance.second_truck_index()[index + 1]), total_distance_2)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]),
                                                                          int(distance.second_truck_index()[
                                                                                  index + 1])), second_leave_times)
        distance.second_truck_list()[index][10] = (str(deliver_package))
        package.get_hash_map().update(int(distance.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass

# Set delivery_start to third_leave_time for all truck three packages -> O(n)
for index, value in enumerate(package.get_final_truck_delivery()):
    package.get_final_truck_delivery()[index][9] = third_leave_times[0]
    third_delivery.append(package.get_final_truck_delivery()[index])

# Compare truck three addresses to address list -> O(n^2)
for index, outer in enumerate(third_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            third_truck_distances.append(outer[0])
            third_delivery[index][1] = inner[0]

# Call algorithm to sort packages for third truck
distance.get_shortest_route(third_delivery, 3, 0)
total_distance_3 = 0

# Calculate total distance of the third truck and distance of each package -> O(n)
for index in range(len(distance.final_truck_index())):
    try:
        total_distance_3 = distance.get_distance(int(distance.final_truck_index()[index]),
                                                 int(distance.final_truck_index()[index + 1]), total_distance_3)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.third_truck_index()[index]),
                                                                          int(distance.third_truck_index()[index + 1])),
                                            third_leave_times)
        distance.third_truck_list()[index][10] = (str(deliver_package))
        package.get_hash_map().update(int(distance.third_truck_list()[index][0]), third_delivery)
    except IndexError:
        pass


# Get distance of all packages -> O(1)
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3
