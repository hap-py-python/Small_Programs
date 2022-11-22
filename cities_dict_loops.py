cities = {'france': 'paris', 'germany': 'munich', 'england': 'london'}

for key, value in cities.items():
    print(f'{value.title()} is in {key.title()}')
print('-'*20)
for city in cities.values():
    print(f'I want to visit {city.title()}')
print('-'*20)
for country in cities:
    print(f'I want to visit {country.title()} next Summer!')


