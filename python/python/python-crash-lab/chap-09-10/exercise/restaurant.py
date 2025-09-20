class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"\nToday's cuisine will be {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is open")

my_restaurant = Restaurant("zammy's kitchen", "ogbono")

print(f"my restaurant's name is {my_restaurant.name}")
print(f"My favourite cuisine is {my_restaurant.cuisine}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()