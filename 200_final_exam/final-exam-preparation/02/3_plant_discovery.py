import re
from statistics import mean


# plants = {'plant':{'rarity': 0, 'rating':[1,2,3]}}

def add_plant(plant, rarity):
    global plants

    if plant not in plants.keys():
        plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants[plant]['rarity'] = rarity


def add_rataing(plant, raining):
    global plants
    plants[plant]['rating'].append(raining)


def update(plant, rarity):
    global plants
    plants[plant]['rarity'] = rarity


def reset(plant):
    plants[plant]['rating'].clear()


plants = dict()

plants_count = int(input())

for _ in range(plants_count):
    command = input()
    plant_rarity = command.split('<->')
    current_plant = plant_rarity[0]
    current_rarity = int(plant_rarity[1])
    add_plant(current_plant, current_rarity)

spliter = r'(\w*): (\w*)( - (\d*))?'
while True:
    command = input()
    if command == 'Exhibition':
        break

    commands = re.search(spliter, command)

    function = commands.group(1)
    plant = commands.group(2)
    if commands.group(4):
        number = int(commands.group(4))

    if plant not in plants.keys():
        print('error')
        continue

    if function == 'Rate':
        add_rataing(plant, number)

    elif function == 'Update':
        update(plant, number)

    elif function == 'Reset':
        reset(plant)

print('Plants for the exhibition:')
for plant, atributes in plants.items():
    average_rating = mean(plants[plant]['rating']) if plants[plant]['rating'] else 0
    rarity = plants[plant]['rarity']
    print(f'- {plant};', end=' ')
    print(f'Rarity: {rarity};', end=' ')
    print(f'Rating: {average_rating:.2f}')
