def repeat(string, reps):
    return string.upper() * reps


def count_uniq(string):
    return len(set(string))



peter_string = input()

current_string = ''
final_string = ''
for index, symbol in enumerate(peter_string):

    if not symbol.isnumeric():
        current_string += symbol
    elif symbol.isnumeric():
        repeats = ''
        for digit in peter_string[index:]:
            if digit.isnumeric():
                repeats += digit
            else:
                break

        repeats = int(repeats)
        final_string += repeat(current_string, repeats)
        current_string = ''


print(f'Unique symbols used: {count_uniq(final_string)}')
print(final_string)
