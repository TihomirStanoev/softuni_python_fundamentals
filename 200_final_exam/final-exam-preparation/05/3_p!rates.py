def plunder(towns, city, plunger_people, plunder_gold):
    total_gold = 0
    total_people = 0
    is_wiped = False

    if towns[city]['population'] - plunger_people <= 0:
        total_people = towns[city]['population']
        is_wiped = True

    else:
        total_people = plunger_people
        towns[city]['population'] -= plunger_people

    if towns[city]['gold'] - plunder_gold <= 0:
        total_gold = towns[city]['gold']
        is_wiped = True

    else:
        total_gold = plunder_gold
        towns[city]['gold'] -= plunder_gold

    print(f'{city} plundered! {total_gold} gold stolen, {total_people} citizens killed.')

    if is_wiped:
        print(f'{city} has been wiped off the map!')
        del towns[city]

    return towns


def prosper(towns,city, prosper_gold):

    if prosper_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        towns[city]['gold'] += prosper_gold
        print(f"{prosper_gold} gold added to the city treasury. {city} now has {towns[city]['gold']} gold.")

    return towns




cities_dict = dict() #{'Name': , {'population': 0, 'gold': 0} }

while True:
    city_command = input()
    if city_command == 'Sail':
        break
    city, people, gold_value = city_command.split('||')
    if city in cities_dict.keys():
        cities_dict[city]['population'] += int(people)
        cities_dict[city]['gold'] += int(gold_value)
    else:
        cities_dict[city] = {'population': int(people), 'gold': int(gold_value)}


commands_list = []
while True:
    commands = input()
    if commands == 'End':
        break
    commands_list.append(commands)


for command in commands_list:
    actions_list = command.split('=>')
    action = actions_list[0]
    town = actions_list[1]

    if action == 'Plunder':
        peoples = int(actions_list[2])
        town_gold = int(actions_list[3])
        cities_dict = plunder(cities_dict,town, peoples, town_gold)

    elif action == 'Prosper':
        town_gold = int(actions_list[2])
        cities_dict = prosper(cities_dict, town, town_gold)




if cities_dict.keys():
    print(f'Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:')
    for city, stocks in cities_dict.items():
        population = stocks['population']
        gold = stocks['gold']

        print(f'{city} -> Population: {population} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")