numbers = [input() for x in range(3)]


if '0' in numbers:
    print('zero')
else:
    sing = lambda x: '-' in x
    count = list(map(sing, numbers)).count(True)
    print('negative') if count % 2 != 0 else print('positive')


# - - - = - 3
# + - - = + 2
# + + - = - 1
# + + + = + 0
# - + + = - 1
# - - + = + 2
