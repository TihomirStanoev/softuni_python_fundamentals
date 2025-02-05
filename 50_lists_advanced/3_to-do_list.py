
elements = []
while True:
    command = input()
    if command == 'End':
        break

    elements.append(command)

indexes = sorted([int(x.split('-')[0]) for x in elements])

to_do_list = [y.split('-')[1] for x in indexes for y in elements if int(y.split('-')[0]) == x]

print(to_do_list)