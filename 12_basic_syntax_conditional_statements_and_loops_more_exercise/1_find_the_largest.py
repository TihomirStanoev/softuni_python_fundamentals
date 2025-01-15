# With lists

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


# With string sorting

number = int(input())

str_number = str(number)

str_biggest = ''.join(sorted(str_biggest, reverse=True))

biggest = int(str_biggest)

print(biggest)

# With a for loop

number_int = int(input())

number = str(number_int)


number_length = len(number)


biggest = ""

for digit in range(0, number_length):
    max_number = max(number)
    biggest += max_number
    for i, x in enumerate(number):
        if x == max_number:
            number = number[:i] + "*" + number[i + 1:]
            break

biggest_int = int(biggest)

print(biggest_int)