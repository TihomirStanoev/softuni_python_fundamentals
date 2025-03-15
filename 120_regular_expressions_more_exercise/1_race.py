import re

names = input().split(', ')

names_dict = {name: 0 for name in names}

while True:
    line = input()
    if line == 'end of race':
        break

    name = re.findall(r'[A-Za-z]', line)
    distance = re.findall(r'\d', line)
    if name and distance:
        name = ''.join(name)
        distance = sum(map(int,distance))

    if name in names_dict.keys():
        names_dict[name] += distance

top_runners = sorted(names_dict.items(), key=lambda distance: -distance[1])

places = ["1st place:", "2nd place:", "3rd place:"]

for place, racer in enumerate(top_runners):
    racer_name, distance = racer
    if place < len(places):
        print(f'{places[place]} {racer_name}')


