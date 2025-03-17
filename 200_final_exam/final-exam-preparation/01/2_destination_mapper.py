import re

text = input()

regex = r'(=|\/)([A-Z][A-Za-z]{2,})\1'

cities = []
points = 0
matches = re.findall(regex, text)

if matches:
    for city in matches:
        cities.append(city[1])
    for city in cities:
        points += len(city)


print('Destinations: ', end='')
print(', '.join(city for city in cities))
print(f'Travel Points: {points}')
