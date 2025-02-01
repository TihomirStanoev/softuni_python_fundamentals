def int_function(int_input):
    return int_input * 2

def real_function(real_input):
    return f'{real_input * 1.5:.2f}'

def string_function(string_input):
    return f'${string_input}$'


read_function = input()
value = input()

number = 0
if read_function == 'int':
    number = int(value)
    print(int_function(number))

elif read_function == 'real':
    number = float(value)
    print(real_function(number))

elif read_function == 'string':
    print(string_function(value))
