def factorial(number):

    factorial_number = 1

    for x in range(1, number + 1):
        factorial_number = factorial_number * x

    return factorial_number


def division(x,y):
    return f'{x / y:.2f}'


a = int(input())
b = int(input())

factorial_a = factorial(a)
factorial_b = factorial(b)

print(division(factorial_a,factorial_b))

# Solution with RECURSION

def factorial(factorial_number):
    if factorial_number <= 1:
        return 1
    else:
        return factorial_number * factorial(factorial_number - 1)

def division(x,y):
    return f'{x / y:.2f}'

a = int(input())
b = int(input())

factorial_a  = factorial(a)
factorial_b = factorial(b)

print(division(factorial_a,factorial_b))