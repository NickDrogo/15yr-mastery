rivers = {'nile river': 'egypt', 'amazon river' : 'brazil', 'yangtza river' : 'china'}


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

print("Rivers included in the dictionary:")

for river in rivers.keys():
    print(river)


print()

print("Countries included in the dictionary:")

for country in rivers.values():
    print(country)



    


