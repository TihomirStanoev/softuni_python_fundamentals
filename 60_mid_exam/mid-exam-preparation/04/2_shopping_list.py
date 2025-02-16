groceries_list = input().split('!')

while True:
    command = input().split()

    if command[0] == 'Go':
        break

    action = command[0]

    if action == 'Urgent':
        item = command[1]
        if item in groceries_list:
            continue
        else:
            groceries_list.insert(0, item)

    elif action == 'Unnecessary':
        item = command[1]
        if item in groceries_list:
            groceries_list.remove(item)

    elif action == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item

    elif action == 'Rearrange':
        item = command[1]
        if item in groceries_list:
            item_index = groceries_list.index(item)
            item = groceries_list.pop(item_index)
            groceries_list.append(item)



print((', ').join(grocery for grocery in groceries_list))