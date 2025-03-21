def contains(key, substring):
    if substring in key:
        return f'{key} contains {substring}'
    return 'Substring not found!'


def flip(key_org, flipper, start, end):
    middle = ''.join(char.lower() if flipper == 'Lower' else char.upper() for char in key_org[start:end])
    return key_org[:start] + middle + key_org[end:]


def slice(act_key, i_start, i_end):
    return act_key[:i_start] + act_key[i_end:]


activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break
    commands = command.split('>>>')
    action = commands[0]

    if action == 'Contains':
        substr = commands[1]
        print(contains(activation_key, substr))
        continue

    elif action == 'Flip':
        start_i = int(commands[2])
        end_i = int(commands[3])
        flip_type = commands[1]
        activation_key = flip(activation_key,flip_type,  start_i, end_i)

    elif action == 'Slice':
        start_i = int(commands[1])
        end_i = int(commands[2])
        activation_key = slice(activation_key, start_i, end_i)

    print(activation_key)
print(f'Your activation key is: {activation_key}')
