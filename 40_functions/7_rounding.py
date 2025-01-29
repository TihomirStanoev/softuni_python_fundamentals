given_numbers = input().split()

numbers = list(map(float, given_numbers))

num_round = lambda a: int(round(a,0))

numbers_round = list(map(num_round,numbers))

print(numbers_round)