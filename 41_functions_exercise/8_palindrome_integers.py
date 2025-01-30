numbers = input().split(', ')

is_palindrome = lambda x: x == x[::-1]

true_false_list = list(map(is_palindrome,numbers))

[print(x) for x in true_false_list]