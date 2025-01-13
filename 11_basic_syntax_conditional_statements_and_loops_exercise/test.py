strin_a = input()
strin_b = input()

transform_st = ''
old_transform = strin_a
l = len(strin_a)


for char in range(l):
    transform_st = strin_b[:char+1] + strin_a[char+1:]

    if transform_st != old_transform:
        print(transform_st)
        old_transform = transform_st

