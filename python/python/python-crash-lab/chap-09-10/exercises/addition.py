
try:
    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
except ValueError:
    print("Please a digit is required")

else:
    result = num1 + num2
    print(result)
