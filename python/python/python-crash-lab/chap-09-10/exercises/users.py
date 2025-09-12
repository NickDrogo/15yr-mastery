class User:

    def __init__(self, first_name, last_name, age, country, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.hobby = hobby
        


    def describe_user(self):
        print(f"\nfirst_name:{self.first_name}")
        print(f"last_name:{self.last_name}")
        print(f"age:{self.age}")
        print(f"county:{self.country}")
        print(f"hobby:{self.hobby}")

    def greet_user(self):
        print(f"\nGreetings to you  dear {self.first_name} {self.last_name}")



user1 = User('Nick', 'Elebeke', 25, 'Nigeria', 'coding')
user2 = User('Zammy', 'Okonkwo', 25, 'Nigeria', 'eating')
user3 = User('Ngozi', 'Mbamara', 42, 'Nigeria', 'chopping money')


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

    