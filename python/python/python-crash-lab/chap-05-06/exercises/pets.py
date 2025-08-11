pet_1 = {
    'animal':'cat',
    'owners_name' : 'kelvin'
    
}

pet_2 = {
    'animal':'rat',
    'owners_name' : 'foden'
    
}

pet_3 = {
    'animal':'lion',
    'owners_name' : 'festus'
}


pets = [pet_1, pet_2, pet_3]

for pet in pets:
        print(f"Animal: {pet['animal']}")
        print(f"owner: {pet['owners_name']}")
        print('-' * 20)