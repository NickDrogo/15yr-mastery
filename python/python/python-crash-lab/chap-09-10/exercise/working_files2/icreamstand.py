class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine


    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"Today's cuisine will be {self.cuisine}\n")

    def open_restaurant(self):
        print(f"{self.name} is open")



class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        self.flavor = ['yoghurt', 'cold_stone', 'dominoes']
        super().__init__(name, cuisine)


    def display_flavor(self):
        print("Here are the flavors:")
        flav = self.flavor
        for flavs in flav:
            print(flavs)
            
    



    
    
my_restaurant = IceCreamStand("zammy's kitchen", "ogbono")
my_restaurant.display_flavor()
