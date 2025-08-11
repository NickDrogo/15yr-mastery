favourite_places = {
    'kelvin':['lagos','abia','uyo'],
    'zamy' : ['finland','ekwulimili','ph'],
    'nick' : ['finland', 'usa', 'singapore']
}

for name, places in favourite_places.items():
    print(f"\n{name.title()} favourite places are :")
    for place in places:
        print(f"\t{place}")
