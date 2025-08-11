car = 'subaru'
print("Is car same as 'subaru' ? I predict True.")
print(car == 'subaru')

print("\nIs car same as 'audi'? I predict False.")
print(car == 'audi')

country = 'Finland'
print("Is number of letters in 'country' = 7❓ I predict True.")
print(len(country) == 7)
print()


age_0 = 25
age_1 = 42

print(age_1 < age_0)
print(age_0 < age_1)

print(age_0 <= age_1)
print(age_0 >= age_1)
print()

country_1 = 'USA'

print('usa' == country_1)
print('usa' == country_1.lower())

print(len(country) > len(country_1))
print(len(country) < len(country_1))
print()

print(age_0 and age_1 <= 60)

print(country == 'USA' or country_1 == 'USA')


cars = ['bmw', 'chevrolet', 'lamborghini', 'porsche', 'ford', 'bugatti']

print()

print('lamborghini' in cars)

print('Mercedez' not in cars)