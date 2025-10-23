def city_country_population(city, country, population=''):
    if population:
        result = f"{city.title()}, {country.title()} -population {population}"
    else:
        result = f"{city.title()}, {country.title()}"
    return result
    



