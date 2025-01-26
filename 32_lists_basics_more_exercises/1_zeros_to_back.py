numbers_str = input().split(', ')

numbers_int = []

for num in numbers_str:
    numbers_int.append(int(num))

non_zero = []
zero = []
for number in numbers_int:
    if number != 0:
        non_zero.append(number)
    else:
        zero.append(number)

number_list = non_zero + zero


print(number_list)
