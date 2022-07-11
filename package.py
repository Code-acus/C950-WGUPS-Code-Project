import datetime

class Package:
    def __init__(self, package_id, address):
        self.package_id = package_id
        self.address = address
        self.delivery_time = None
        self.loading_time = None
        self.earliest_loading_time = datetime.time(8, 0, 0)
        self.mileage = 0

    def is_delivered(self):
        return self.delivery_time is not None

    def is_not_delivered(self):
        return not self.is_delivered()

    def deliver(self, delivery_time, mileage):
        self.delivery_time = delivery_time
        self.mileage = mileage

    def __str__(self):
        return "Package ID: " + str(self.package_id) + " Address: " + str(self.address) + " Delivery Time: " \
               + str(self.delivery_time) + " Loading Time: " + str(self.loading_time) + " Earliest Loading Time: " \
               + str(self.earliest_loading_time) + " Mileage: " + str(self.mileage)

    def print_package_status_for_time(self, requested_time, start_time):
        status = "enroute"

        if requested_time < start_time:
            status = "at hub"

        elif self.delivery_time is None:
            status = "enroute"

        elif requested_time > self.delivery_time:
            status = "delivered"

        return "Package ID: " + str(self.package_id) + " Address: " + str(self.address) + " Delivery Time: " \
               + str(self.delivery_time) + " Loading Time: " + str(self.loading_time) + " Earliest Loading Time: " \
               + str(self.earliest_loading_time) + " Mileage: " + str(self.mileage) + " Status: " + status

