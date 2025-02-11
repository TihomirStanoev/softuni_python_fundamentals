def loot(inventory, items):
    for item in items:
        if item not in inventory:
            inventory.insert(0, item)

    return inventory


def drop(inventory, i):
    if 0 <= i < len(inventory):
        item = inventory.pop(i)
        inventory.append(item)

    return inventory


def steal(inventory, count):
    steal_items = inventory[-count:]
    del inventory[-count:]
    print(', '.join(item for item in steal_items))

    return inventory


def calculate_treasure(treasures):
    total_treasure = sum(len(treasure) for treasure in treasures)
    count_treasure = len(treasures)

    if count_treasure == 0:
        return 0
    return total_treasure / count_treasure


def treasure_hunt(list_of_items):

    while True:
        command = input().split()

        if command[0] == 'Yohoho!':
            average = calculate_treasure(list_of_items)
            return list_of_items, average



        action = command[0]
        list_with_commands = command[1:]

        if action == 'Loot':
            list_of_items = loot(list_of_items, list_with_commands)

        elif action == 'Drop':
            index = int(list_with_commands[0])
            list_of_items = drop(list_of_items, index)

        elif action == 'Steal':
            items = int(list_with_commands[0])
            list_of_items = steal(list_of_items, items)




initial_loot = input().split('|')

initial_loot, treasure_average = treasure_hunt(initial_loot)

if initial_loot:
    print(f'Average treasure gain: {treasure_average:.2f} pirate credits.')
else:
    print("Failed treasure hunt.")