class Bakery:
    def __init__(self):
        self.food_list = []


    def get_input(self):
        str_list = input().split()
        self.food_list.extend(str_list)

    def bakery_dict(self):
        keys = []
        values = []
        for i in range(len(self.food_list)):
            if i % 2 == 0:
                keys.append(self.food_list[i])
            else:
                value = int(self.food_list[i])
                values.append(value)

        return dict(zip(keys, values))


baker = Bakery()
baker.get_input()
print(baker.bakery_dict())
