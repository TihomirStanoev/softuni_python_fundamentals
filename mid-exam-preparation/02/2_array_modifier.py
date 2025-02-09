integers_array = list((map(int, input().split())))


while True:
    command = input().split()

    if command[0] == 'end':
        break

    action = command[0]

    if action == 'swap':
        first_index, second_index = int(command[1]), int(command[2])
        integers_array[first_index], integers_array[second_index] = integers_array[second_index], integers_array[first_index]

    elif action == 'multiply':
        first_index, second_index = int(command[1]), int(command[2])
        integers_array[first_index] *= integers_array[second_index]

    elif action == 'decrease':
        integers_array = [x - 1 for x in integers_array]


print(', '.join(str(x) for x in integers_array))