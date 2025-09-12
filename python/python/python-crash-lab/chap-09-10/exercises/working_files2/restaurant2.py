class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"Today's cuisine will be {self.cuisine}")
        

    def open_restaurant(self):
        print(f"{self.name} is open")
    
    def number_customer_served(self):
        print(f"we have served {self.number_served} amount of people today\n")

    def increment_number(self, number_of_customers):
        self.number_served += number_of_customers


my_restaurant = Restaurant("zammy's kitchen", "Ofe ogbono")
my_restaurant.describe_restaurant()
my_restaurant.number_customer_served()

my_restaurant.describe_restaurant()
my_restaurant.number_served = 23
my_restaurant.number_customer_served()


my_restaurant.describe_restaurant()
my_restaurant.increment_number(100)
my_restaurant.number_customer_served()


