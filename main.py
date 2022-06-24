# Harrison Rogers, Student ID: 00632898

class Main:
    # This is the message the user will see displayed when the program starts
    # The interface is accessible from here
    def __init__(self):
        self.main()

    def main(self):
        print("----------------------------------------------")
        print("THE WGUPS - PARCEL AND PACKAGE ROUTING SYSTEM.")
        print("----------------------------------------------")
        # FIXME: Add additional code for the interface return message here

        user_input = input("Please select from the options below:"
                           "1. Get status for all packages for a particular time frame"
                           "2. Get status single package for a particular time frame"
                           "3. Quit to exit the package query ")    # Get user input

        while user_input is not "3. Quit to exit the package query":
            if user_input == "1":
                print("Please enter a time in the format HH:MM:SS")
                user_input = input()
                print("The packages that were delivered at " + user_input + " are:")
