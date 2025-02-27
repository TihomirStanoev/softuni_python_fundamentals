def dict_create(list_from_chars):
    keys = []
    values = []

    for char in list_from_chars:
        keys.append(char)
        values.append(ord(char))

    return dict(zip(keys, values))



char_list = input().split(', ')

print(dict_create(char_list))