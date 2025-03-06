def emoticon_finder(string):
    emoji_list = []
    for i in range(len(string)):
        is_emoji = ''
        char = string[i]
        if char == ":":
            is_emoji += string[i:i+2]
        if is_emoji:
            emoji_list.append(is_emoji)

    return '\n'.join(emoji_list)


sentence = input()

print(emoticon_finder(sentence))

