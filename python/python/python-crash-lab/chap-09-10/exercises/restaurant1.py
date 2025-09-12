class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"Today's cuisine will be {self.cuisine}\n")

    def open_restaurant(self):
        print(f"{self.name} is open")

my_restaurant = Restaurant("zammy's kitchen", "ogbono")
igbo_restaurant = Restaurant("Kitches", 'Ofe Nsala')
one_is_one = Restaurant("popular", 'Ofe Onugbu')

my_restaurant.describe_restaurant()
igbo_restaurant.describe_restaurant()
one_is_one.describe_restaurant()