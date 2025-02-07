message = input().split()

decipher_message = []

for word in message:
    first_letter_str = ''
    second_part = []
    the_word = ''
    for symbol in word:
        if symbol.isdecimal():
            first_letter_str += symbol
        else:
            second_part.append(symbol)

    first_letter = chr(int(first_letter_str))

    the_word += first_letter
    second_part[0], second_part[-1] = second_part[-1], second_part[0]

    the_word += ''.join(second_part)
    decipher_message.append(the_word)

print(' '.join(decipher_message))
