sides = dict()


def user_exist(current_user):
    user_exist = False
    for side, users in sides.items():
        if current_user in users:
            user_exist = True
            break

    return user_exist


def add_user_side(new_side, new_user):
    if new_side not in sides.keys():
        sides[new_side] = []

    user_in_side = user_exist(new_user)
    if not user_in_side:
        sides[new_side].append(new_user)

'''
def change_user_side(name, change_side):
    exist = user_exist(name)

    if exist and change_side in sides.keys():
        user_current_side = ''.join(side for side, users in sides.items() if name in users)
        user_index = sides[user_current_side].index(name)
        sides[user_current_side].pop(user_index)
        sides[change_side].append(name)

    else:
        add_user_side(change_side, name)

    return f'{name} joins the {change_side} side!'
'''

def change_user_side(name, change_side):
    user_current_side = None
    for side, users in sides.items():
        if name in users:
            user_current_side = side
            break

    if user_current_side:
        sides[user_current_side].remove(name)
    else:
        add_user_side(change_side, name)

    add_user_side(change_side, name)

    return f'{name} joins the {change_side} side!'

def results():
    result = ''
    for k, v in sides.items():
        if len(v) != 0:
            result += f'Side: {k}, Members: {len(v)}\n'
            for u in v:
                result += f'! {u}\n'

    return result


def users():
    while True:
        command = input()
        if command == 'Lumpawaroo':
            break

        if '|' in command:
            side, user = command.split(' | ')
            add_user_side(side, user)


        elif '->' in command:
            user, side = command.split(' -> ')
            print(change_user_side(user, side))


users()
print(results())
