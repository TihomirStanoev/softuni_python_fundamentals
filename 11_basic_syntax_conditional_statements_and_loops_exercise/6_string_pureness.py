strings_n = int(input())

type = ''
for _ in range(strings_n):
    string = input()

    if ',' in string or '.' in string or '_' in string:
        type = ' is not pure!'
    else:
        type = ' is pure.'

    print(string+type)