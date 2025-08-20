prompt = "Enter a series of pizza toppings please:\n "



while True:
    pizza_toppings = input(prompt)
    
    if pizza_toppings == 'quit':
        break
    else:
        print(f"I'll add {pizza_toppings} to your pizza")

    
