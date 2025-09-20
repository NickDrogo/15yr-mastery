import json
from pathlib import Path

def favourite_num():
    path =  Path('chap09&10/working_files1/fav_num.json')
    user_num = input("Enter your favourite num: ")
    contents = json.dumps(user_num)
    path.write_text(contents)


favourite_num()

def show_favourite_num():
    path = Path('chap09&10/working_files1/fav_num.json')
    result = path.read_text()
    contents = json.loads(result)
    print(f"I know your favourite number, it is {contents}")


show_favourite_num()

