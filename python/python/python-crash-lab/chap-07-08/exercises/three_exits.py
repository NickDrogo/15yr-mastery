prompt = print("Please, Enter your age\n")

user_choice = int(input())

active = True
while active:
    if user_choice < 3:
        print("\nYour ticket is free")
        user_choice = input("Enter 'quit' to exit\n")

        if user_choice == 'quit':
            break
        
    elif user_choice >= 3 and user_choice <= 12:
        print("\nYour ticket is $1o")
        active = False

    else:
        print("\nYour ticket is $15")
        break


