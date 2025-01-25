level_of_fire = input().split('#')
amount_of_water = int(input())


total_effort = 0.0
cells = []

for levels in level_of_fire:
    is_valid = False

    levels_list = levels.split(" = ")

    type_of_fire = levels_list[0]
    fire_value = int(levels_list[-1])

    if type_of_fire == "Low" and  (1 <= fire_value <= 50):
        is_valid = True
    elif type_of_fire == "Medium" and (51 <= fire_value <= 80):
        is_valid = True
    elif type_of_fire == "High" and (81 <= fire_value <= 125):
        is_valid = True

    if is_valid:
        if (amount_of_water - fire_value) < 0:
            continue

        cells.append(fire_value)
        effort = fire_value * 0.25
        total_effort += effort
        amount_of_water -= fire_value


print('Cells:')
[print("- " + (str(cell))) for cell in cells]
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells)}")