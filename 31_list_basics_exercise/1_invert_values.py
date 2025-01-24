single_string = input()

string_list = single_string.split(' ')

#print(string_list)

opposite = []
#opposite2 = [int(_) * -1 for _ in string_list]

for _ in string_list:
    _ = int(_)
    opposite.append(_ * -1)

print(opposite)
