
from country import city_country


def test_cities_country():
        format_Citycountry = city_country('abuja','nigeria')
        assert format_Citycountry == 'Abuja, Nigeria'

    

 
