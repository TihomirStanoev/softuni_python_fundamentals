class InventoryItems:
    def __init__(self):
        self.items = []

    def get_items(self):
        self.items = input().split()


class Stock:
    def __init__(self):
        self.stock = {}

    def get_stock(self):
        item_stock = input().split()

        item = [item_stock[i] for i in range(len(item_stock)) if i % 2 == 0]
        dict_stock = [int(item_stock[i]) for i in range(len(item_stock)) if i % 2 != 0]

        self.stock = dict(zip(item, dict_stock))


class Inventory:
    def __init__(self, store_stock, search_items):
        self.store_stock = store_stock
        self.search_items = search_items

    def __str__(self):
        result = ''
        for item in self.search_items:
            if item not in self.store_stock.keys():
                result += f'Sorry, we don\'t have {item}\n'
            else:
                result += f'We have {self.store_stock[item]} of {item} left\n'

        return result



stock = Stock()
inventory_items = InventoryItems()

stock.get_stock()
inventory_items.get_items()

stock_dict = stock.stock
inventory_list = inventory_items.items

print(Inventory(stock_dict, inventory_list))



