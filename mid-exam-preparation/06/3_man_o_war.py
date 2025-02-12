def fire(warship_list: list, i: int, damage: int):
    if i in range(len(warship_list)):
        warship_list[i] -= damage

        if warship_list[i] <= 0:
            print('You won! The enemy ship has sunken.')
            return True, warship_list

    return False, warship_list


def defend(pirate_list: list, i_start: int, i_end:int, damage: int):
    if i_start in range(len(pirate_list)) and i_end in range(len(pirate_list)):

        for section in range(i_start, i_end + 1):
            pirate_list[section] -= damage
            if pirate_list[section] <= 0:
                print('You lost! The pirate ship has sunken.')
                return True, pirate_list

    return False, pirate_list


def repair(pirate_list: list, i: int, health: int, health_maximum: int):
    if i in range(len(pirate_list)):
        if pirate_list[i] + health >= health_maximum:
            pirate_list[i] = health_maximum
        else:
            pirate_list[i] += health

    return pirate_list


def status(pirate: list, health_maximum: int):
    lower_value = health_maximum * 0.2

    return sum(section < lower_value for section in pirate)


def section_status(ship: list):
    return sum(ship)


def man_o_war(pirate: list, warship: list, health_max: int):
    is_lose = False
    while True:
        command = input().split()

        if command[0] == 'Retire':
            break

        action = command[0]

        if action == 'Fire':
            index = int(command[1])
            given_damage = int(command[2])
            is_win, warship = fire(warship, index, given_damage)
            if is_win:
                is_lose = True
                break

        elif action == 'Defend':
            start_index = int(command[1])
            end_index = int(command[2])
            given_damage = int(command[3])
            is_lost, pirate = defend(pirate, start_index, end_index, given_damage)
            if is_lost:
                is_lose = True
                break

        elif action == 'Repair':
            index = int(command[1])
            given_health = int(command[2])
            pirate = repair(pirate, index, given_health, health_max)


        elif action == 'Status':
            total_section = status(pirate, health_max)
            print(f'{total_section} sections need repair.')

    return pirate, warship, is_lose


pirate_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
maximum_health = int(input())

pirate_status, warship_status, lose = man_o_war(pirate_status, warship_status, maximum_health)

if not lose:
    pirate_sum = section_status(pirate_status)
    warship_sum = section_status(warship_status)

    print(f'Pirate ship status: {pirate_sum}')
    print(f'Warship status: {warship_sum}')
