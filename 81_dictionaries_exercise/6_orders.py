def get_items():
    collected_products = {}

    while True:
        command = input().split()
        if 'buy' in command:
            break

        product, price, quantity = command[0], float(command[1]), int(command[2])

        if product in collected_products.keys():
            collected_products[product]['price'] = price
            collected_products[product]['quantity'] += quantity
        else:
            collected_products[product] = {}
            collected_products[product]['price'] = price
            collected_products[product]['quantity'] = quantity

    return collected_products


def calculate_total(products_qty):
    result = ''
    for product, key in products_qty.items():
        total = products_qty[product]['price'] * products_qty[product]['quantity']
        result += f'{product} -> {total:.2f}\n'

    return result


products = get_items()
print(calculate_total(products))
