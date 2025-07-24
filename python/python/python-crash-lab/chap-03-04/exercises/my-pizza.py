my_pizza = ['Dominoes', 'Chicken Republic', 'Pepperoni']

friend_pizza = my_pizza[:]

my_pizza.append("kdr")
friend_pizza.append("mr biggs")

print("my favourite pizzas are")

for pizza in my_pizza:
    print(pizza)

print()

print("my friends favourite pizzas are")
for pizza in friend_pizza:
    print(pizza)