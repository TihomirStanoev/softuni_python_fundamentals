def add_stop(all_stops, start, string):
    if 0 <= start < len(all_stops):
        return all_stops[:start] + string + all_stops[start:]
    return all_stops


def remove_stops(all_stops, start, end):
    if 0 <= start < len(all_stops) and 0 <= end < len(all_stops):
        return all_stops[:start] + all_stops[end + 1:]
    return all_stops


def switch(all_stops, old, new):
    if old in all_stops:
        return all_stops.replace(old, new)
    return all_stops


stops = input()

while True:
    command = input()
    if command == 'Travel':
        break

    command_list = command.split(":")
    action = command_list[0]

    if action == 'Add Stop':
        index, string = int(command_list[1]), command_list[2]
        stops = add_stop(stops, index, string)

    elif action == 'Remove Stop':
        start_index, end_index = int(command_list[1]), int(command_list[2])
        stops = remove_stops(stops, start_index, end_index)

    elif action == 'Switch':
        old_string, new_string = command_list[1], command_list[2]
        stops = switch(stops, old_string, new_string)

    print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
