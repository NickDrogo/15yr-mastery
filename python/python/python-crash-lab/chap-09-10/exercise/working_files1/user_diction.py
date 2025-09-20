import json
from pathlib import Path

def get_stored_user_info():
        path = Path('chap09&10/working_files1/user_info.json')
        if path.exists():
                info = path.read_text()
                if info:
                        contents = json.loads(info)
                        for keys, values in contents.items():
                              print(f"{keys} : {values}")
                
                else:
                    data = {}
                    username = input("What is your name? ")
                    data['name'] = username

                    user_state = input("What is your state?: ")
                    data['state'] = user_state

                    user_age = input("What is your age?: ")
                    data['age'] = user_age

                    contents = json.dumps(data)
                    path.write_text(contents)
                    print("We'll rememeber your info next time")
        
        else:
            print("the file does not exist")

get_stored_user_info()