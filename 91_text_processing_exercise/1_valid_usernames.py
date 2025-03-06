def name_check(names_list):
    symbols = ['_','-']
    valid_names = []

    for name in names_list:
        if len(name) in range(3,16):
            is_valid = False
            for char in name:
                if char.isalnum() or char in symbols:
                    is_valid = True
                else:
                    is_valid = False
                    break

            if is_valid:
                valid_names.append(name)

    return '\n'.join(valid_names)


names = input().split(', ')
print(name_check(names))