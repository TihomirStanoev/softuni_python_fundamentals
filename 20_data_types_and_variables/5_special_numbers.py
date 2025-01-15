number = int(input())

str_number = str(number)

special_numbers = [5, 7, 11]

for numbers in range(1, number + 1):
    digits = str(numbers)
    digit_sum = 0
    digit_list = []
    for digit in digits:
        digit_list.append(int(digit))
    print(f'{numbers} -> True') if sum(digit_list) in special_numbers else print(f'{numbers} -> False')

