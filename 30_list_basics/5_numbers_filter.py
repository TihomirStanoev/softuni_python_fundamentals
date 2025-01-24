numbers = int(input())

number_list = [int(input()) for number in range(numbers)]

command = input()

# •	even
# •	odd
# •	negative
# •	positive

filtered_list = []

if command == 'even':
    filtered_list = [even for even in number_list if even % 2 == 0]
elif command == 'odd':
    filtered_list = [odd for odd in number_list if odd % 2 != 0]
elif command == 'negative':
    filtered_list = [negative for negative in number_list if negative < 0]
else:
    filtered_list = [positive for positive in number_list if positive >= 0]

print(filtered_list)