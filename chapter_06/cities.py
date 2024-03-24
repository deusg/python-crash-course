# 6-11.

cities = {
    'dar es salaam': {
        'country': 'tanzania',
        'population': 8_161_231,
        'fact': 'Dar es Salaam is an Arabic phrase that translates to "abode of peace"'

    },

    'nairobi': {
        'country': 'kenya',
        'population': 4_397_000,
        'fact': 'The name “Nairobi” comes from the Maasai phrase "Enkare Nyrobi", which translates to “cool water”'

    },

    'kampala': {
        'country': 'uganda',
        'population': 1_650_800,
        'fact': "The name Kampala comes from the local Bugandan name K'empala, which means 'Hill of the Impala'"
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is in {country}.")
    print(f"- {city.title()} has population of {population}.")
    print(f"- Interesting fact about: {fact}.")
    


