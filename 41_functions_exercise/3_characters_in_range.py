def char_rec(value):
    value += 1
    if value == ord_b:
        return ''
    print(chr(value), end =' ')
    return char_rec(value)


str_a = input()
str_b = input()

ord_a = ord(str_a)
ord_b = ord(str_b)

print(char_rec(ord_a))