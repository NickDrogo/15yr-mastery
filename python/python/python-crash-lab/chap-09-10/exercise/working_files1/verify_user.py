import json

from pathlib import Path



def get_stored_username(path):

    if path.exists:
        contents = path.read_text()
        username = json.loads(contents)
        return username

    else:
        return None



def get_new_username(path):
    username = input("what is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    path = Path('Notes/files/username.json')
    username = get_stored_username(path)
    if username:
        confirm = input(f"Is '{username}' the correct usernam (y/n): ")
        if confirm == 'y':
            print(f"Welcome back, {username}!")
        
        elif confirm == 'n':
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}")
            

    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}")



greet_user()