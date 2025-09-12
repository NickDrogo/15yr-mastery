file_name = 'chap09&10/working_files/cats.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
    
else:
    print(contents)

print()

file = 'chap09&10/working_files/dogs.txt'

try:
    with open(file) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
    
else:
    print(contents)

print()

file = 'chap09&10/working_files/dog.txt'

try:
    with open(file) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
    
else:
    print(contents)
