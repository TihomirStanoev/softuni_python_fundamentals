numbers = list(map(int, input().split(', ')))

to_number = max(numbers)

for number in range(10, to_number+10, 10):
    print(f'Group of {number}\'s: ', end='')
    numbers_list = []
    for number_for_group in numbers:
        if number >= number_for_group > number-10:
            numbers_list.append(number_for_group)
    print(numbers_list)

