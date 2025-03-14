import re

def cost_calc(price, qty):
    return price * qty


regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
total_amount = 0
furniture_list = []


while True:
    command = input()
    if command == 'Purchase':
        break
    items = re.search(regex, command)

    if items:
        furniture = items.group(1)
        furniture_price = float(items.group(2))
        quantity = int(items.group(3))

        total_amount += cost_calc(furniture_price, quantity)
        furniture_list.append(furniture)


print('Bought furniture:')
for fur in furniture_list:
    print(fur)
print(f'Total money spend: {total_amount:.2f}')