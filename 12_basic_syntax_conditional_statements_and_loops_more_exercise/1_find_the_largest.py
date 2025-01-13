number = int(input())

str_number = str(number)

list_number = []
for char in str_number:
    list_number.append(char)

list_number.sort(reverse=True)

str_biggest = ''
for char in list_number:
    str_biggest += char


biggest = int(str_biggest)

print(biggest)