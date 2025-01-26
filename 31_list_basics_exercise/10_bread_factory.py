total_energy = 100
total_coins = 100

working_day_events = input().split('|')

for day_event in working_day_events:
    event, ingredient_str = day_event.split('-')
    ingredient = int(ingredient_str)

    if event == 'rest': # 90 - 30  | 100
        if total_energy + ingredient >= 100:
            gained_energy = 100 - total_energy
        else:
            gained_energy = ingredient

        total_energy += gained_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')


    elif event == 'order':
        if total_energy - 30 >= 0:
            total_coins += ingredient
            total_energy -= 30
            print(f'You earned {ingredient} coins.')

        else:
            total_energy += 50
            print('You had to rest!')

    else:
        if total_coins - ingredient >= 0:
            print(f'You bought {event}.')
            total_coins -= ingredient
        else:
            print(f'Closed! Cannot afford {event}.')
            break

else:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f'Energy: {total_energy}')