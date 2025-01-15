number = int(input())

str_num = str(number)

while True:
    number += 1
    str_number = str(number)

    if len(set(str_number)) == len(str_number):
        print(number)
        break


