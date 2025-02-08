integers_list = list(map(int,input().split()))

total_sum = 0
while True:
    if not integers_list:
        break

    given_index = int(input())

    if given_index < 0:
        removed_element = integers_list[0]
        total_sum += removed_element
        integers_list[0] = integers_list[-1]

    elif len(integers_list) <= given_index:
        removed_element = integers_list[-1]
        total_sum += removed_element
        integers_list[-1] = integers_list[0]

    else:
        removed_element = integers_list.pop(given_index)
        total_sum += removed_element

    for element in range(len(integers_list)):
        if integers_list[element] <= removed_element:
            integers_list[element] += removed_element
        else:
            integers_list[element] -= removed_element



print(total_sum)