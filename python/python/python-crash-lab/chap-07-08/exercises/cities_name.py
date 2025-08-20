def city_names(city, country):
    return f"{city.title()}, {country.title()}"

result = city_names('aso rock', 'nigeria')
result1 = city_names('nnewi', 'nigeria')
result2 = city_names('chicago', 'america')

print(result)
print(result1)
print(result2)