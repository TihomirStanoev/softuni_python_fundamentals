houses = list(map(int,input().split('@')))


current_index = 0
mission_success = True
while True:
    command = input().split()

    if command[0] == 'Love!':
        break

    jump = int(command[1])
    jump_on = current_index + jump
    current_index += jump

    if jump_on <= len(houses)-1:
        houses[jump_on] -= 2
        current_index = jump_on
    else:
        current_index = 0
        houses[current_index] -= 2

    if houses[current_index] == 0:
        print(f'Place {current_index} has Valentine\'s day.')
    elif houses[current_index] < 0:
        print(f'Place {current_index} already had Valentine\'s day.')



print(f'Cupid\'s last position was {current_index}.')

filed_houses = sum(1 for x in houses if x > 0)


if filed_houses == 0:
    print('Mission was successful.')
else:
    house_count = len(list(filter(lambda x: x>0, houses)))
    print(f'Cupid has failed {house_count} places.')