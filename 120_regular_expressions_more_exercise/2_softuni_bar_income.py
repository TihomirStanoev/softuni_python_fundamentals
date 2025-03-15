import re



regex = r'%([A-Z][a-z]+)%<(\w+)>.*?\|(\d+)\|.*?((\d+(\.\d+)?)\$)$' #70

total_income = 0
while True:
    line = input()
    if line == 'end of shift':
        break

    customer = re.search(regex, line)
    if customer:
        name, product, qty, price = customer.group(1),customer.group(2),int(customer.group(3)),float(customer.group(4))
        total = qty * price
        total_income += total
        print(f'{name}: {product} - {total:.2f}')


print(f'Total income: {total_income:.2f}')