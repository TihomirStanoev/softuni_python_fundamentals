
numbers_str = input().split()
given_string = input()

number_sums = []
for nu in numbers_str:
    sum_el = 0
    for el in nu:
        sum_el += int(el)
    number_sums.append(sum_el)

chars = []
given_list = list(given_string)
for number_sum in number_sums: # 29
    char = ''
    string_len = len(given_list)

    index = 0
    length = 0

    while True:
        if number_sum == length:
            char = given_list.pop(index)
            chars.append(char)
            break
        length += 1
        index += 1
        if index == string_len:
            index = 0


print(''.join(ch for ch in chars))