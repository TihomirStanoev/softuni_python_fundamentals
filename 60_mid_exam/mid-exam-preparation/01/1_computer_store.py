values_list = []
type_of_calculation = ''
while True:
    command = input()

    if command == 'special' or command == 'regular':
        type_of_calculation = command
        break

    value = float(command)

    if value <= 0:
        print('Invalid price!')
        continue

    values_list.append(value)



if not values_list:
    print('Invalid order!')
else:
    total_value = sum(values_list)
    tax = total_value * 0.2
    final_price = total_value + tax

    if type_of_calculation == 'special':
       final_price *= 0.9


    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_value:.2f}$')
    print(f'Taxes: {tax:.2f}$')
    print('-----------')
    print(f'Total price: {final_price:.2f}$')