def perfect_number(num):
    divisor_sum = 0
    is_perfect = False

    for divisor in range(1, num):
        if num % divisor == 0:
            divisor_sum += divisor

    if num % divisor_sum == 0:
        is_perfect = True

    return is_perfect



number = int(input())

if perfect_number(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')