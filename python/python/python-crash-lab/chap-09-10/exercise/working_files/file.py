from pathlib import Path
file_name = 'chap09&10/working_files/learning_python.txt'

path = Path(file_name)
contents = path.read_text()
print(contents)

print()


path = Path(file_name)
contents = path.read_text()

pi_string = contents.splitlines()

for line in pi_string:
    print(f"- {line}")


print()


path = Path(file_name)
contents = path.read_text()


for line in contents.splitlines():
    print(f"- {line}")



    