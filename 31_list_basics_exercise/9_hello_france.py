TICKET_PRICE = 150

collection_of_items = input().split('|')
budget = float(input())

purchased_items = []

for items in collection_of_items:
    item_list = items.split('->')
    item = item_list[0]
    price = float(item_list[1])

    if item == 'Clothes':
        if price > 50.00:
            continue
    elif item == 'Shoes':
        if price > 35.00:
            continue
    elif item == 'Accessories':
        if price > 20.50:
            continue


    if budget < price:
        continue

    budget -= price
    purchased_items.append(price)

new_price = []

for price in purchased_items:
    price *= 1.40
    new_price.append(price) # round

difference = []

for profit in range(len(purchased_items)):
    item_profit = new_price[profit] - purchased_items[profit]
    difference.append(item_profit) # round

profit = sum(difference)
total_profit = sum(new_price)
total_money = total_profit + budget



print(' '.join(f'{amount:.2f}' for amount in new_price))
print(f'Profit: {profit:.2f}')
if total_money >= TICKET_PRICE:
    print('Hello, France!')
else:
    print('Not enough money.')

