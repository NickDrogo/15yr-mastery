import json


file_name = 'fav_num.json'

try:
    with open(file_name) as f:
        fav_num = json.load(f)

except (FileNotFoundError,
    json.JSONDecodeError):    
    fav_num = input("Enter your favorite number: ")
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
    print("Got it")

else:
    print(f"it's {fav_num}")