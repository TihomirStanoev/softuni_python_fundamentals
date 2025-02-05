wagons = [0] * int(input())

while True:
    command = input()
    if command == 'End':
        break

    actions_split = command.split()
    action = actions_split[0]

    if action == 'add':
        add = int(actions_split[1])
        wagons[-1] += add

    elif action == 'insert' or action == 'leave':
        index = int(actions_split[1])
        people = int(actions_split[2])

        if action == 'insert':
            wagons[index] += people
        else:
            wagons[index] -= people


print(wagons)