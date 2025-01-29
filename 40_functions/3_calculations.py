#"multiply", "divide", "add", and "subtract".

def multiply(a,b):
    return a * b

def divide(a,b):
    return  int(a / b)

def add(a,b):
    return a + b

def subtract(a,b):
    return  a - b


operator = input()
a = int(input())
b = int(input())

result = 0
if operator == 'multiply':
    result = multiply(a, b)
elif operator == 'divide':
    result = divide(a, b)
elif operator == 'add':
    result = add(a, b)
elif operator == 'subtract':
    result = subtract(a,b)

print(result)
