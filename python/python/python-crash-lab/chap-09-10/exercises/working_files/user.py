first_name = input("Enter your first name:\n")
last_name = input("Enter your last name:\n")

file_name = 'chap09&10/working_files/guest.txt'

with open(file_name, 'a') as file_object:
    file_object.write(f"{first_name} {last_name}")