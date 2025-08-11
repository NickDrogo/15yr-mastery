favourite_num = {
    'Nick': [20,80],
    'kelvin': [10,67],
    'zamy' : [5,80],
    'collins': [8,9],
    'phillip' : [3,63]
}



for name, numbers in favourite_num.items():
    print(f"\n{name}'s favourite numbers are: ")
    for number in numbers:
        print(f"\t{number}")