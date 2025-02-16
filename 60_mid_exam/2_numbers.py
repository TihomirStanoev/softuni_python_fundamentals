numbers = list(map(int,input().split()))


while True:
    command = input().split()
    if command[0] == 'Finish':
        break

    action = command[0]
    value = int(command[1])

    if action == 'Add':
        numbers.append(value)

    elif action == 'Remove':
        if value in numbers:
            index_for_remove = numbers.index(value)
            del numbers[index_for_remove]

    elif action == 'Replace':
        if value in numbers:
            replace_value = int(command[2])
            old_value = numbers.index(value)
            numbers[old_value] = replace_value

    elif action == 'Collapse':
        numbers = [number for number in numbers if number >= value]




print(' '.join(str(number) for number in numbers))