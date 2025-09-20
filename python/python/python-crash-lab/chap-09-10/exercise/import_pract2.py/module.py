from module1 import User

class Privileges:
    def __init__(self):
            self.privileges = ['can add post', 'can delete post', 'can ban user', 'can send notifications']


    def show_priviledges(self):
        print("Here are the administrator's set of priviledges")
        priv = self.privileges
        for priviledge in priv:
            print(priviledge)
            


class Admin(User):
    def __init__(self, first_name, last_name, age, country, hobby):
        super().__init__(first_name, last_name, age, country, hobby)
        self.privileges = Privileges()


