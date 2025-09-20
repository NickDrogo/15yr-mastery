from pathlib import Path
path =  Path('chap09&10/working_files/files/cats.txt' )

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} doesn not exist")
else:
    print(contents)



path =  Path('chap09&10/working_files/files/dogd.txt' )
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"sorry, the file {path} does not exist")
else:
    print(contents)
