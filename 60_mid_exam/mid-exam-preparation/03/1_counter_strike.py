initial_enerty = int(input())

command = input()

win_balles = 0

is_lose = False
while True:
    if command == "End of battle":
        break

    distance = int(command)
    current_energy = initial_enerty

    current_energy -= distance

    if current_energy >= 0:
        initial_enerty = current_energy
    else:
        is_lose = True
        break


    win_balles += 1

    if win_balles % 3 == 0:
        initial_enerty += win_balles

    command = input()

if is_lose:
    print(f'Not enough energy! Game ends with {win_balles} won battles and {initial_enerty} energy')
else:
    print(f'Won battles: {win_balles}. Energy left: {initial_enerty}')