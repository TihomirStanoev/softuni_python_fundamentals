def get_user():
    users = dict()
    while True:
        command = input().split(' -> ')
        if command[0] == 'End':
            break
        company, user = command

        if company not in users.keys():
            users[company] = [user]
        else:
            if user not in users[company]:
                users[company].append(user)

    return users



def result_print(company_dict):
    result = ''
    for company, user in company_dict.items():
        result += f'{company}\n'
        for user_id in user:
            result += f'-- {user_id}\n'

    return result



users_dict = get_user()
print(result_print(users_dict))

