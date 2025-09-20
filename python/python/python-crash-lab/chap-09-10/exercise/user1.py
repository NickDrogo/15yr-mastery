class User:

    def __init__(self, first_name, last_name, age, country, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.hobby = hobby
        self.login = 0


    def describe_user(self):
        print(f"\nfirst_name:{self.first_name}")
        print(f"last_name:{self.last_name}")
        print(f"age:{self.age}")
        print(f"county:{self.country}")
        print(f"hobby:{self.hobby}")

    def greet_user(self):
        print(f"\nGreetings to you  dear {self.first_name} {self.last_name}")
 
    def login_attempt(self):
        self.login += 1
        return self.login
        

    def reset_login_attempt(self):
        self.login = 0
        return self.login

user1 = User('Nick', 'Elebeke', 25, 'Nigeria', 'coding')


user1.describe_user()
user1.greet_user()

print(user1.login_attempt())
print(user1.login_attempt())
print(user1.reset_login_attempt())

