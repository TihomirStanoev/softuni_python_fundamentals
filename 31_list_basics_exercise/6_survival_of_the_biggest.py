string_list = input().split()
numbers_for_remove = int(input())

list_of_integer = [int(x) for x in string_list]

sorted_list = list_of_integer.copy()

sorted_list.sort(reverse=True)

for x in range(numbers_for_remove):
    sorted_list.pop()

filtered_list = []

for x in list_of_integer:
    if x in sorted_list:
        filtered_list.append(x)


print(', '.join(str(char) for char in filtered_list))