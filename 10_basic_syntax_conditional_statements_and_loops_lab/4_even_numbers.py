numbers = int(input())

counter = 0

for _ in range(numbers):
    n = int(input())
    if n % 2 != 0:
        print(f'{n} is odd!')
        break
    counter += 1


if counter == numbers:
    print("All numbers are even.")