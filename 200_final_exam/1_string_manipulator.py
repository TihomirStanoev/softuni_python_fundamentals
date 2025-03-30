def translate(translate_string, char, replacement):
    translating_string = translate_string.replace(char, replacement)
    print(translating_string)
    return translating_string

def includes(translate_string, substring):
    result = 'False'
    if substring in translate_string:
        result = 'True'
    return result

def start(string, start_substring):
    start_l = len(start_substring)
    result = 'False'

    if start_substring == string[:start_l]:
        result = 'True'

    return result


def lowercase(my_string):
    lowercase_string = my_string.lower()
    print(lowercase_string)
    return lowercase_string

def find_index(string, finding_char):
    last_index = 0
    for i, char in enumerate(string):
        if char == finding_char:
            last_index = i

    return last_index


def remove(remove_from, start_index, count):
    start_string = remove_from[:start_index]
    last_part = remove_from[start_index+count:]
    return start_string + last_part





received_string = input()

commands = []
while True:
    command = input()
    if command == 'End':
        break
    commands.append(command)

for single_command in commands:
    commands_list = single_command.split()
    action = commands_list[0]

    if action == 'Translate':
        given_char, given_replacement = commands_list[1], commands_list[2]
        received_string = translate(received_string, given_char, given_replacement)


    elif action == 'Includes':
        given_substring = commands_list[1]
        res = includes(received_string, given_substring)
        print(res)


    elif action == 'Start':
        given_substring = commands_list[1]
        res = start(received_string, given_substring)
        print(res)

    elif action == 'Lowercase':
        received_string = lowercase(received_string)

    elif action == 'FindIndex':
        given_char = commands_list[1]
        index = find_index(received_string, given_char)
        print(index)

    elif action == 'Remove':
        start, number_char = int(commands_list[1]), int(commands_list[2])
        received_string = remove(received_string,start, number_char)
        print(received_string)
