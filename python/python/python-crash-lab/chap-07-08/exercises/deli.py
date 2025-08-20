sandwich_orders = ['club sandwich', 'blt', 'grilled cheese', 'submarine sandwich', 'panini']

finished_sandwich = []

while sandwich_orders:
    orders = sandwich_orders.pop()
    print(f"I made your {orders}")
    finished_sandwich.append(orders)
    

print('\nHere are the list of sandwiches that was made:')
for result in finished_sandwich:
    print(result)