import re

text_string = input()
regex = r'(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
mirror_word = []

# matches = re.finditer(regex, text_string)
matches = re.findall(regex, text_string)

if matches:
    print(f'{len(matches)} word pairs found!')
    for match in matches:
        first_word = match[1]
        second_word = match[2]
        if first_word == second_word[::-1]:
            mirror_word.append(f'{first_word} <=> {second_word}')


else:
    print('No word pairs found!')

if mirror_word:
    print('The mirror words are:')
    print(', '.join(mirror_word))
else:
    print('No mirror words!')
