def merge(merge_list, start, end):

    if start not in range(len(merge_list)):
        start = 0
    if end not in range(len(merge_list)):
        end = len(merge_list)-1

    list_start = merge_list[:start]
    list_end = merge_list[end + 1:]

    marged_list = [''.join(merge_list[index] for index in range(start, end+1))]

    merge_list = list_start + marged_list + list_end
    return merge_list


def divide(divide_list, index, parts):
    list_start = divide_list[:index]
    list_end = divide_list[index + 1:]
    divide_string = divide_list[index]

    finish_list = []
    starting_point = 0
    step = len(divide_string)//parts
    for _ in range(parts):
        if _ == parts - 1:
            finish_list.append(divide_string[starting_point:])
            break
        else:
            finish_list.append(divide_string[starting_point:starting_point + step])

        starting_point += step

    divide_list = list_start + finish_list + list_end

    return divide_list



given_string = input().split()

while True:
    command = input().split()
    if '3:1' in command:
        break

    action, start_index_str, end_index_str = command
    start_index = int(start_index_str)
    end_index = int(end_index_str)



    if action == 'merge':
        given_string = merge(given_string, start_index, end_index)
    elif action == 'divide':
        given_string = divide(given_string, start_index,end_index)


print(' '.join(given_string))