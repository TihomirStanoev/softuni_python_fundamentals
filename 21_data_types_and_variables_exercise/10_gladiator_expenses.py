lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet, broken_sword, broken_shield, broken_armor = 0,0,0,0

for fight in range(1, lost_fights_count + 1):

    if fight % 2 == 0:
        broken_helmet += 1

    if fight % 3 == 0:
        broken_sword += 1

    if fight % 2 == 0 and fight % 3 == 0:
        broken_shield += 1
        if broken_shield % 2 == 0:
            broken_armor += 1


expenses =   ((broken_helmet * helmet_price)
                + (broken_sword *  sword_price)
                + (broken_shield * shield_price)
                + (broken_armor *  armor_price))

print(f'Gladiator expenses: {expenses:.2f} aureus')