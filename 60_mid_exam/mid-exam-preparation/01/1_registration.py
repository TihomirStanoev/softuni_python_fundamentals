def letters(command_name, case):

    if case == 'Lower':
        command_name = command_name.lower()
    elif case == 'Upper':
        command_name = command_name.upper()

    return command_name

def reverse(reversed_str, start, end):
    new_string = reversed_str[start:end+1]
    new_string = new_string[::-1]

    if new_string in reversed_str:
        return reversed_str
    return new_string


def substring(sub_name, substr):
    if substr in sub_name:
        return sub_name.replace(substr, '')
    return f'The username {sub_name} doesn\'t contain {substr}.'

def rreplace(name_string, reapalced_char):
    return name_string.replace(reapalced_char,'-')

def is_valid(name_valid, given_char):
    if given_char in name_valid:
        return 'Valid username.'
    return f'{given_char} must be contained in your username.'



name = input()



while True:
    command = input().split()
    function = command[0]
    if function == 'Registration':
        break

    if function == 'Letters':
        name = letters(name, command[1])
        print(name)

    elif function == 'Reverse':
        i_start = int(command[1])
        i_end = int(command[2])

        if 0 <= i_start <= i_end < len(name):
            print(reverse(name, i_start,i_end))
        else:
            continue

    elif function == 'Substring':
        parameter = command[1]
        print(substring(name, parameter))

    elif function == 'Replace':
        name = rreplace(name,command[1])
        print(name)
    elif function == 'IsValid':
        print(is_valid(name, command[1]))
