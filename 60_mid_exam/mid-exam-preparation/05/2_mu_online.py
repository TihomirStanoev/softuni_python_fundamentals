initial_health = 100
initial_bitcoins = 0

def potion(health_current, amount):
    if health_current + amount >= 100:
        amount = 100 - health_current
        health_current = 100
    else:
        health_current += amount

    return  health_current, amount


def chest(bitcoin, amount):
    return bitcoin + amount


def fight(total_health, attack):
    return total_health - attack


def mu_online(health, bitcoins, rooms):

    for room_number, room in enumerate(rooms, start=1):
        room_commands = room.split()
        action, value_string = room_commands
        value = int(value_string)

        if action == 'potion':
            health, value = potion(health,value)
            print(f'You healed for {value} hp.')
            print(f'Current health: {health} hp.')

        elif action == 'chest':
            bitcoins = chest(bitcoins, value)
            print(f'You found {value} bitcoins.')

        else:
            monster = action
            health = fight(health, value)
            if health > 0:
                print(f'You slayed {monster}.')
            elif health <= 0:
                return health, bitcoins, f'You died! Killed by {monster}.', room_number, False

    return health, bitcoins, 'You\'ve made it!', None, True



room_list = input().split('|')

current_health, current_bitcoins, status, room, is_win = mu_online(initial_health, initial_bitcoins, room_list)


if is_win:
    print(status)
    print(f'Bitcoins: {current_bitcoins}')
    print(f'Health: {current_health}')
else:
    print(status)
    print(f'Best room: {room}')