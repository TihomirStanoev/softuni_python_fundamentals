targets = list(map(int,input().split()))

while True:
    command = input().split()

    if command[0] == 'End':
        break

    action = command[0]
    index = int(command[1])


    if action == 'Shoot':
        power = int(command[2])
        if index >= 0 and index <= len(targets)-1:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        value = int(command[2])
        if index >= 0 and index <= len(targets)-1:
            targets.insert(index,value)
        else:
            print('Invalid placement!')


    elif action == 'Strike':
        radius = int(command[2])
        left_index = index - radius
        right_index = index + radius

        if left_index >= 0 and right_index < len(targets):
            target_range = (radius * 2) + 1
            for _ in range(target_range):
                targets.pop(left_index)

        else:
            print('Strike missed!')
            continue


print('|'.join(str(x) for x in targets))