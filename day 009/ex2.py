travel_log = [
    {
        'country': 'France',
        'visited': 12,
        'cities': ['Paris', 'Lillie','Dijon']
    },
    {
        'country': 'Germany',
        'visited': 5,
        'cities': ['Berlin', 'Hamburg','Stuttgart']
    },
]

def add_new_country(country, visited, cities):
    new_entry = {}
    new_entry['country'] = country
    new_entry['visited'] = visited
    new_entry['cities'] = cities
    travel_log.append(new_entry)
    

add_new_country('Russia', 5, ['Moscow', 'Saint Petersburg'])
print(travel_log) 