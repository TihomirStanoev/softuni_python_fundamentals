import re


def calculate_threshold(digi_list):
    threshold = 1
    for number in digi_list:
        threshold *= int(number)

    return threshold


def emoji_points(emoji_):
    points = 0
    for char in emoji_:
        points += ord(char)

    return points


def emoji_calculate(emoji_list):
    emojies = dict()
    for moji, sym, word in emoji_list:
        emojies[moji] = emoji_points(word)

    return emojies


word_rex = r'((\:\:|\*\*)([A-Z][a-z]{2,})\2)'
digi_rex = r'\d'

some_text = input()

digits = re.findall(digi_rex, some_text)
emoji = re.findall(word_rex, some_text)

total_threshold = calculate_threshold(digits)
emoji_dict = emoji_calculate(emoji)

print(f"Cool threshold: {total_threshold}")
print(f"{len(emoji_dict.keys())} emojis found in the text. The cool ones are:")
for emji, point in emoji_dict.items():
    if point > total_threshold:
        print(emji)