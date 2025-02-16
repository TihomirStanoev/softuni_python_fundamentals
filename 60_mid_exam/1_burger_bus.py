cities = int(input())

total_profit = 0

for _ in range(cities):
    city_number = _ + 1
    profit = 0
    city = input()
    income = float(input())
    expenses = float(input())

    if city_number % 3 == 0:
        expenses *= 1.5
        if city_number % 5 == 0:
            expenses /= 1.5

    if city_number % 5 == 0:
        income *= 0.9

    profit = income - expenses

    total_profit += profit
    print(f'In {city} Burger Bus earned {profit:.2f} leva.')

print(f'Burger Bus total profit: {total_profit:.2f} leva.')
