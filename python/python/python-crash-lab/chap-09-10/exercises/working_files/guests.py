
file_name = 'chap09&10/working_files/guest_book.txt'

while True:
    
    first_name = input("Enter your first name:\n")
    last_name = input("Enter your last name:\n")
     
    with open(file_name, 'a') as file_object:
        file_object.write(f"{first_name.title()} {last_name.title()}\n")
        print(f"Dear {first_name} {last_name}, your visit has been recorded")
        break



        
