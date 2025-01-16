numbers = int(input())
# ord('a') = 97

rng = range(0, numbers)
ord_a = ord('a') # 97
ord_b = ord('a') # 97
ord_c = ord('a') # 97
end = ord('a') + numbers

for a in rng:
    for b in rng:
        for c in rng:
            print(f'{chr(ord_a)}{chr(ord_b)}{chr(ord_c)}')
            ord_c += 1
            if ord_c == end:
                ord_c = 97
                break
        ord_b += 1
        if ord_b == end:
            ord_b = 97
            break
    ord_a += 1
    if ord_a == end:
        ord_a = 97
        break
