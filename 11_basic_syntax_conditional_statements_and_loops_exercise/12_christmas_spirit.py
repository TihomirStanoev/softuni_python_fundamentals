quantity_of_decorations = int(input())
days_left = int(input())

ornament_price, ormanemt_points = 2, 5
skirt_price, skirt_points =	5, 3
garland_price, garland_points = 3, 10
lights_price, lights_points = 15, 17

total_price = 0
total_spirit = 0

for day in range(1,days_left+1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_price += ornament_price * quantity_of_decorations
        total_spirit += ormanemt_points
    if day % 3 == 0:
        total_price += (skirt_price + garland_price) * quantity_of_decorations
        total_spirit += skirt_points + garland_points
    if day % 5 == 0:
        total_price += lights_price * quantity_of_decorations
        total_spirit += lights_points
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_price += skirt_price + garland_price + lights_price


if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")