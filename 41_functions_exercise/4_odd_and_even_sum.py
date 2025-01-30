def total_sum(number_list):
    even_list = []
    odd_list = []

    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return sum(even_list), sum(odd_list)


str_input = input()


int_list = list(map(int,str_input))

even_sum, odd_sum = total_sum(int_list)

print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')