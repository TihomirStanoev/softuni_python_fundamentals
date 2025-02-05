names_list = list(input().split(', '))


names_sorted_aph = sorted(names_list, key=lambda x: (-len(x),x))

print(names_sorted_aph)