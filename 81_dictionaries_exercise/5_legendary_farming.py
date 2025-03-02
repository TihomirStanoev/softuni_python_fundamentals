key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
winners = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

win = False
while not win:
    items_str = input().split()

    for index in range(0, len(items_str), 2):
        item, qty = items_str[index + 1].lower(), int(items_str[index])

        if item not in key_materials.keys():
            key_materials[item] = 0
        key_materials[item] += qty

        for d_key in winners.keys():
            if key_materials[d_key] >= 250:
                key_materials[d_key] -= 250
                print(f'{winners[d_key]} obtained!')
                win = True
                break

        if win:
            break

print('\n'.join(f'{k}: {i}' for k, i in key_materials.items()))
