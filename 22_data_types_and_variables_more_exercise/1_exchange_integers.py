number_a = int(input())
number_b = int(input())


print(f'Before:\na = {number_a}\nb = {number_b}')

number = number_a
number_a = number_b
number_b = number

print(f'After:\na = {number_a}\nb = {number_b}')

