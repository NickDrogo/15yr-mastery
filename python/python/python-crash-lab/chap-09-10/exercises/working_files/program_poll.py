file_name = 'chap09&10/working_files/poll.txt'

while True:
    user_reason = input("Why do you like programming:\n")

    with open(file_name, 'a') as file_object:
        
        file_object.write(f"{user_reason}\n")
        print("Have you listed all your reasons")
        
        reply = input("Enter (y/n)")
        if reply == 'y':
            break
        elif reply == 'n':
            continue