from population import city_country_population

def test_city_country_population():
    full_details = city_country_population('abuja','nigeria',675000 )
    assert full_details ==  "Abuja, Nigeria -population 675000"
