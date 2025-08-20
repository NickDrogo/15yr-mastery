sandwich_orders = ['club sandwich', 'pastrami', 'blt', 'pastrami', 'grilled cheese', 'submarine sandwich', 'panini', 'pastrami']

finished_sandwich = []

print("\nThe deli has ran out of pastrami")

while sandwich_orders:
    
    while 'pastrami' in sandwich_orders:

        orders = sandwich_orders.remove('pastrami')    
    orders = sandwich_orders.pop()
    print(f"I made your {orders}")
    finished_sandwich.append(orders)
    

print('\nHere are the list of sandwiches that was made:')
for result in finished_sandwich:
    print(result)