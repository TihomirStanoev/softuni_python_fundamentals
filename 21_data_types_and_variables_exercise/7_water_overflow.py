tank_capacity = 255

number_of_lines = int(input())

total_sum = 0
liters_sum = 0

for water in range(0, number_of_lines):
    liters = int(input())

    if liters_sum + liters <= tank_capacity:
        liters_sum += liters
        continue
    else:
        print("Insufficient capacity!")


print(liters_sum)