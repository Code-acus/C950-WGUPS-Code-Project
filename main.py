# Harrison Rogers, Student ID: 00632898

class Main:
    def __init__(self):
        self.main()

    def main(self):
        print("----------------------------------------------")
        print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
        print("----------------------------------------------")
        print("ROUTE DELIVERIES - COMPLETED SUCCESSFULLY...\n")
        # FIXME: Add code here to print out the route deliveries

        user_input = input()
        print(""" Please select an option or type 'quit' to exit: \n 1. To get package details for a particular time 
        \n 2. To get details on a single package for a particular time """)

        while user_input != "quit":
            if user_input == "1":
                print("Please enter a time in the format HH:MM:SS")
                user_input = input()
                print("The packages that were delivered at " + user_input + " are:")

