numbers = input().split(', ')


indexes = [i for i,x in enumerate(numbers) if int(x) % 2 == 0]

print(indexes)