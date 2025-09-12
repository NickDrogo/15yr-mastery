import random

my_ticket = [1,2,3,4,5,6,7,8,9]

count = 0

while True:
    choice = random.choice(my_ticket)

    if choice != 9:
        count += 1
        continue

    elif choice == 9:
        count += 1
        print(f"It took {count} amount of times to get a winning ticket")
        break




    

    

    



    