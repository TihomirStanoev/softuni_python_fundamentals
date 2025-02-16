top = []

for emp in range(3):
    add = int(input())
    top.append(add)

sudents = int(input())

top.sort(reverse=True)

hours = 0

while sudents > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    for emp in top:
        sudents -= emp
        if sudents <= 0:
            break

print(f'Time needed: {hours:.0f}h.')



