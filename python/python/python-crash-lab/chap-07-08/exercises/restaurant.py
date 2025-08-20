restaurant_seating = "How many are in the dinner group? "

restaurant_seating = int(input(restaurant_seating))

if restaurant_seating > 8:
    print("\nSorry, they will have to wait for a table")

else:
    print("\nYour table is ready.")