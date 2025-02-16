def collect(collected_items, item):
    if item not in collected_items:
        collected_items.append(item)

    return collected_items


def drop(dropped_items, item):
    if item in dropped_items:
        index = dropped_items.index(item)
        dropped_items.pop(index)

    return dropped_items


def combine_items(combined_items, old_item, new_item):
    if old_item in combined_items:
        index = combined_items.index(old_item)
        combined_items.insert(index+1, new_item)

    return combined_items


def renew(renew_items, item):
    if item in renew_items:
        index = renew_items.index(item)
        item = renew_items.pop(index)
        renew_items.append(item)

    return renew_items



def inventory(items):

    while True:
        command = input().split(' - ')

        if command[0] == 'Craft!':
            return ', '.join(items)

        action, item = command[0], command[1]

        if action == 'Collect':
            items = collect(items, item)
        elif action == 'Drop':
            items = drop(items, item)
        elif action == 'Combine Items':
            item_list = item.split(':')
            item, new_item = item_list
            items = combine_items(items, item, new_item)
        elif action == 'Renew':
            items = renew(items, item)



collecting_items = list(input().split(', '))
print(inventory(collecting_items))