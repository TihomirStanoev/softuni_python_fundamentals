coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

def total_calculate(product, quantity):
    total = 0

    if product == 'coffee':
        total = coffee * quantity
    elif product == 'water':
        total = water * quantity
    elif product == 'coke':
        total = coke * quantity
    elif product == 'snacks':
        total = snacks * quantity

    return total


purchased_product = input()
qty = int(input())

total_price = total_calculate(purchased_product, qty)

print(f'{total_price:.2f}')