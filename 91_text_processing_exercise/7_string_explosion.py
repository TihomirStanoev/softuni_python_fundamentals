def explosion(text):
    total_explosions = 0
    text_after_explosion = ''
    for i, char in enumerate(text):
        if char == '>':
            total_explosions += int(text[i+1])
            text_after_explosion += char

        elif total_explosions > 0:
            total_explosions -= 1

        else:
            text_after_explosion += char

    return text_after_explosion


text_before = input()
print(explosion(text_before))
