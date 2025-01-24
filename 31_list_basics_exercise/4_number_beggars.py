baggar_str = input()
turns = int(input())


baggar_list = baggar_str.split(', ')
baggar_list = [int(baggars) for baggars in baggar_list]


index = 0
baggar_sum = [0] * turns

for baggar in baggar_list:
    baggar_sum[index] += baggar
    index += 1
    if index == turns:
        index = 0

print(baggar_sum)