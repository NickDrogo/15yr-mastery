
class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")
    
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer:   
          self.odometer = mileage 
        else:
            print("You can't roll back an odometer!")
 
    
    def increment_odometer(self, miles):
        self.odometer += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge.")





class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


    
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()





