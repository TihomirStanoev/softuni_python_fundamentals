factor = int(input())
count = int(input())


numbers = []

for multiples in range(1, count+1):
    multiples *= factor
    numbers.append(abs(multiples))

print(numbers)
