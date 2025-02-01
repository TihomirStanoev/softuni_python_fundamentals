from math import  floor

def coordinates_check(coordinates_list):

    closest_zero = sum(map(abs,coordinates_list[0])) # 6
    closest_zero_set = []

    for x, y in coordinates_list:
        cooridnates_difference = abs(x) + abs(y)

        if cooridnates_difference <= closest_zero:
            closest_zero_set.clear()
            closest_zero_set.append(x)
            closest_zero_set.append(y)
            closest_zero = cooridnates_difference



    return f'({floor(closest_zero_set[0])}, {floor(closest_zero_set[1])})'


coordinates = []


for xy in range(2):
    xy_list = []
    x = float(input())
    xy_list.append(x)

    y = float(input())
    xy_list.append(y)

    coordinates.append(xy_list)


print(coordinates_check(coordinates))