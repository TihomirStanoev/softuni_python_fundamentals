targets_str = input().split()
targets = [int(x) for x in targets_str]

command = input()

shot_targets = 0

while True:
    if command == 'End':
        break

    shot = int(command)

    if len(targets) <= shot or shot < 0:
        command = input()
        continue


    if targets[shot] != -1:
        value = targets[shot]
        targets[shot] = -1

        for index in range(len(targets)):
            if targets[index] <= value and targets[index] > 0:
                targets[index] += value

            elif targets[index] > value:
                targets[index] -= value


    shot_targets += 1

    command = input()


print(f'Shot targets: {shot_targets} -> ', end='')
print(' '.join(str(x) for x in targets))
