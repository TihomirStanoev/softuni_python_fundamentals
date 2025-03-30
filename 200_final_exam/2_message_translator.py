import re

def get_ascii(some_text):
    return ' '.join(str(ord(char)) for char in some_text)


numbers_commands = int(input())

regex = r'(!)([A-Z][a-z]{2,})\1\:\[([A-Za-z\s]+)\]'

for _ in range(numbers_commands):
    command = input()

    match = re.search(regex, command)

    if match:
        new_command = match.group(2)
        message_ascii = get_ascii(match.group(3))
        print(f'{new_command}: {message_ascii}')

    else:
        print("The message is invalid")