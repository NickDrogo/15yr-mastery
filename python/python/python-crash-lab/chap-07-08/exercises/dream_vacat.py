responses = {}

polling_user = True

while polling_user:
    name = input("What is your name\n")
    place = input("\nWhat's your dream vacation:")

    responses[name] = place

    repeat = input("\nWould you like another person to respond? (yes/no)")
    if repeat == 'no':
        polling_user = False
    

print("\n---poll results---")

for name, place in responses.items():
    print(f"{name} would like to visit {place}")

