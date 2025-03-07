def letter_position(letter):
    return ord(letter) & 31


def last_letter_calculation(letter, num):
    position = letter_position(letter)
    sums = 0

    if letter.isupper():
        sums = num - position
    elif letter.islower():
        sums = num + position

    return sums


def first_letter_calculation(letter, num):
    position = letter_position(letter)
    sums = 0

    if letter.isupper():
        sums = num / position
    elif letter.islower():
        sums = num * position

    return sums


string_list = input().split()

total_sum = 0
for change in string_list:
    letters = ''
    number = ''
    for symbol in change:
        if symbol.isalpha():
            letters += symbol
        elif symbol.isdigit():
            number += symbol

    first_letter, second_letter = letters
    number = int(number)

    number = first_letter_calculation(first_letter,number)
    total_sum += last_letter_calculation(second_letter,number)


print(f'{total_sum:.2f}')
