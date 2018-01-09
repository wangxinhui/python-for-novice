class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = self.year + ' ' + self.make + ' ' + self.model
        return  long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_date(self,meliage):
        if meliage >= self.odometer_reading:
            self.odometer_reading = meliage
        else:
            print("You cat't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles



