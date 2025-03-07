def remove_dubs(text):
    clear_text = ''

    for index, char in enumerate(text):
        if index == len(text)-1:
            if char == text[-1]:
                clear_text += char
            break
        if char != text[index+1]:
            clear_text += char

    return clear_text


text_string = input()

print(remove_dubs(text_string))
