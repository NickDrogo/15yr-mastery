import json
from pathlib import Path

path = Path('chap09&10/working_files1/fav_num.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favourite number! It's {number}")
else:
    number = input("What's your favourite number ?: ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Got it! I'll remember your favorite number.")