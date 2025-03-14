import re


class User:
    def __init__(self):
        self.furnitures = dict()
        self.furniture_id = 0

    def add_furniture(self, furniture_type, price, qty):
        self.furnitures[self.furniture_id] = dict()
        self.furnitures[self.furniture_id]['furniture'] = furniture_type
        self.furnitures[self.furniture_id]['price'] = price
        self.furnitures[self.furniture_id]['quantity'] = qty
        self.furniture_id += 1


class FurnitureShop:
    def __init__(self, user_furniture):
        self.user_furniture = user_furniture

    def calculate_total(self):
        total_cost = 0

        for ID, furniture in self.user_furniture.items():
            total_cost += furniture['price'] * furniture['quantity']

        return f'{total_cost:.2f}'

    def item_list(self):
        furnitures_str = ''

        for ID, furniture in self.user_furniture.items():
            furnitures_str += furniture['furniture']
            furnitures_str += '\n'

        return furnitures_str.strip()


user_items = User()

while True:
    items = input()
    if items == 'Purchase':
        break

    regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
    found_item = re.search(regex, items)
    if found_item:
        furniture = found_item.group(1)
        furniture_price = float(found_item.group(2))
        quantity = int(found_item.group(3))

        user_items.add_furniture(furniture, furniture_price, quantity)

result = FurnitureShop(user_items.furnitures)

print('Bought furniture:')
print(result.item_list())
print(f'Total money spend: {result.calculate_total()}')
