rows = int(input())

columns = 0
for r in range(rows):
    columns += 1
    for c in range(columns):
        print("*", end='')
    print('\n', end='')

for r in range(rows):
    columns -= 1
    for c in range(columns):
        print("*", end='')
    print('\n', end='')
