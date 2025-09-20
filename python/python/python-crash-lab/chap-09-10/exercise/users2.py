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
    



class Admin(User):
    def __init__(self, first_name, last_name, age, country, hobby):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can send notifications']
        super().__init__(first_name, last_name, age, country, hobby)

    def show_priviledges(self):
        print("Here are the administrator's set of priviledges")
        priv = self.privileges
        for priviledge in priv:
            print(priviledge)



user1 = Admin('Nick', 'Elebeke', 25, 'Nigeria', 'coding')
user1.show_priviledges()




