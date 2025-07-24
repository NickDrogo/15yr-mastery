cars = 'lamborghini', 'Chevrolet', 'Rolls Royce', 'Mercedes Benz', 'BMW'

lst = list(cars)
print(lst)

lst.append("Ford")
print(lst)

lst.insert(0, "Camaro")
print(lst)

lst.remove("Camaro")
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

print(sorted(lst))
print(lst)

print(sorted(lst, reverse=True))
print(lst)

del lst[0]
print(lst)

print(f"{lst.pop(0)} is here by popped")

lst.reverse()
print(lst)

print(len(lst))
