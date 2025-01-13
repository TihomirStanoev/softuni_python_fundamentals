number_of_orders = int(input())

total_price = 0
price = 0.0

for order in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())

    if days < 1 or days > 31:
        continue
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if  capsules < 1 or capsules > 2000:
        continue

    price = price_per_capsule * days * capsules
    print(f'The price for the coffee is: ${price:.2f}')
    total_price += price

print(f"Total: ${total_price:.2f}")