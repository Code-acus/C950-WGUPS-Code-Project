import csv
import datetime

with open('./data/distance_data.csv') as csvfile1:
    distance_data = list(csv.reader(csvfile1, delimiter=','))
with open('./data/time_data.csv') as csvfile2:
    distance_name_data = list(csv.reader(csvfile2, delimiter=','))

    # Calculate package address data - should run in O(n)
    # Explain what you are doing with this code and why you are using the following code:
    def get_address():
        return distance_data


    # Calculate total dist from the given row and column values - should run in O(n)
    # Explain what you are doing with this code and why you are using the following code:
    def get_distance(row, column, total):
        dist = distance_data[row][column]
        if dist == '':
            dist = distance_data[column][row]

        return total + float(dist)


    # Calculate given dist for a truck - should run in O(n)
    def get_time(dist, truck_list):
        new_time = dist / 18
        dist_in_minutes = new_time * 60
        final_time = datetime.timedelta(minutes=dist_in_minutes)
        truck_list.append(final_time)
        for i in truck_list:
            (hrs, mins, secs) = str(i).split(':')
            final_time += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return final_time


    # Represent the lists of sorted trucks that are in order of efficiency and referenced in the following functions
    first_truck_index[]
    first_truck_indices[]
    # #
    second_truck[]
    second_truck_indices[]
    # #
    third_truck[]
    third_truck_indices[]

    # The algorithm uses a greedy approach to find the optimal solution using recursion to find the best location
    # for each truck to vist next with regard to distance and time it takes to visit the next location and is a
    # based on the current location of the truck.

    # The algorithm has three parameters including: 1) the list of packages, 2) the truck number,
    # and 3) the current location of the given truck

    # Lastly, a recursive call is made for the next location and shortened list.
    # Recursive calls will continue to be made until the base case is called, which will
    # end the function and return the now empty list.

    # Base Case: Length of the list is False, or zero.

    # Space-Time Complexity should run in O(n^2)

    def get_shortest_route(
            _list,
            num,
            curr_location,
            first_truck=None,
            first_truck_indices=None,
            second_truck=None,
            second_truck_indices=None,
            third_truck=None,
            third_truck_indices=None):

        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if get_distance(curr_location, value) <= lowest_value:
                lowest_value = get_distance(
                    curr_location, value)
                location = value

        for i in _list:
            if get_distance(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_truck.append(i)
                    first_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 1, curr_location)
                elif num == 2:
                    second_truck.append(i)
                    second_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 2, curr_location)
                elif num == 3:
                    third_truck.append(i)
                    third_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 3, curr_location)


    # Insert 0 for the first index of each index list
    first_truck_index.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')

    # The following are all helper functions to return a desired value and should run in O(1)
    def first_truck_index(first_truck=None):
        return first_truck

    def first_truck_list(first_truck=None):
        return first_truck

    def second_truck_index(second_truck_indices=None):
        return second_truck_indices

    def second_truck_list(second_truck=None):
        return second_truck

    def third_truck_index(third_truck_indices=None):
        return third_truck_indices

    def third_truck_list(third_truck=None):
        return third_truck
