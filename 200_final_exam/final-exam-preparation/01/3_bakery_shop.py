foods = dict()
product_sold = 0
def receive(qty, food):
    global foods

    if food in foods.keys():
        foods[food] += qty
    else:
        foods[food] = qty

def sell(qty, food):
    global foods, product_sold

    if food not in foods.keys():
        return f"You do not have any {food}."

    if foods[food] > qty:
        foods[food] -= qty
        product_sold += qty
        return f"You sold {qty} {food}."
    elif foods[food] == qty:
        product_sold += qty
        del foods[food]
        return f"You sold {qty} {food}."
    elif foods[food] < qty:
        sold_quantity = foods[food]
        product_sold += foods[food]
        del foods[food]
        return f"There aren't enough {food}. You sold the last {sold_quantity} of them."


while True:
    commands = input()
    if commands == 'Complete':
        break

    command, quantity, product = commands.split()
    quantity = int(quantity)

    if command == 'Receive':
        receive(quantity,product)
    elif command == 'Sell':
        print(sell(quantity, product))


for product, qty in foods.items():
    print(f'{product}: {qty}')


print(f'All sold: {product_sold} goods')