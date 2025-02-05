text = input()

text_without_vowels = ''.join(x for x in text if x.lower() not in 'aouei')

print(text_without_vowels)