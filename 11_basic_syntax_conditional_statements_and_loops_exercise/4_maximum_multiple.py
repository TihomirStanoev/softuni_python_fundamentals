divisor = int(input())
boundary = int(input())


for _ in range(boundary):
    if boundary % divisor == 0:
        print(boundary)
        break
    boundary = boundary - 1