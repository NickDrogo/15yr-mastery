import json

def favourite_num():

    filename = 'fav_num.json'

    user = input("Enter favourite num: ")
    
    with open(filename, 'w') as f:
        json.dump(user, f)



favourite_num()

def show_favourite_num():
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            user = json.load(f)
            print(f"I know your favourite number, it is {user}")
    except FileNotFoundError:
        print("file name does not exist!")

show_favourite_num()

