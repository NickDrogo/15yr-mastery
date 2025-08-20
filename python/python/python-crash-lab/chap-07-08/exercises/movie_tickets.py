prompt = print("Please, Enter your age\n")

user_choice = int(input())

while True:
    if user_choice < 3:
        print("\nYour ticket is free")
        break
    
    elif user_choice >= 3 and user_choice <= 12:
        print("\nYour ticket is $1o")
        break

    else:
        print("\nYour ticket is $15")
        break


