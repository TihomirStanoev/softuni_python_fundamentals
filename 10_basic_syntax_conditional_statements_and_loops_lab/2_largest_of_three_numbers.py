num1 = int(input())
num2 = int(input())
num3 = int(input())


num = num1

if num >= num2 and num >= num3:
    print(num)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

