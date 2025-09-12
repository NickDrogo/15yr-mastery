file_name = 'chap09&10/working_files/learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

    
print()

with open(file_name) as file_object:
    contents = file_object.readlines()
    for line in contents:
        print(line.rstrip())

print()


with open(file_name) as file_object:
    contents = file_object.readlines()


pi_string = ''

for line in contents:
    pi_string += line.rstrip()
    print()

python_talks = input("Do you want to know what i love about python, enter (y/n): ")

if python_talks == 'y':
    print(pi_string)

else:
    print("That's fine! Thanks for not wasting our time.")


    
