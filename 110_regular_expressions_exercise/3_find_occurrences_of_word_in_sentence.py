import re


sentence = input()
word = input()

regex = r'\b'

for letter in word:
    regex += f'[{letter.upper()}{letter.lower()}]'
regex += r'\b'

matches = re.findall(regex, sentence)

print(len(matches))