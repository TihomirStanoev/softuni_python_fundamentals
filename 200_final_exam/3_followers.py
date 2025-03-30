def new_follower(followers_dict, username):
    if username not in followers_dict.keys():
        followers_dict[username] = {'likes': 0, 'comments': 0}

    return followers_dict

def like(followers_dict, username, count):
    if username in followers_dict.keys():
        followers_dict[username]['likes'] += count
    else:
        followers_dict[username] = {'likes': count, 'comments': 0}

    return followers_dict

def comment(followers_dict, username):
    if username in followers_dict.keys():
        followers_dict[username]['comments'] += 1
    else:
        followers_dict[username] = {'likes': 0, 'comments': 1}

    return followers_dict

def blocked(followers_dict, username):
    if username in followers_dict.keys():
        del followers_dict[username]
    else:
        print(f"{username} doesn't exist.")

    return followers_dict



followers = dict() # {'name': {'likes': 0, 'comments': 0}}


commands = []
while True:
    command = input()
    if command == 'Log out':
        break
    commands.append(command)


for current_command in commands:
    commands_list = current_command.split(': ')
    action = commands_list[0]

    if action == 'New follower':
        current_username = commands_list[1]
        followers = new_follower(followers, current_username)

    elif action == 'Like':
        current_username, current_counts = commands_list[1], int(commands_list[2])
        followers = like(followers, current_username, current_counts)

    elif action == 'Comment':
        current_username = commands_list[1]
        followers = comment(followers, current_username)

    elif action == 'Blocked':
        current_username = commands_list[1]
        followers = blocked(followers, current_username)


print(f'{len(followers.keys())} followers')
for username, likes_comments in followers.items():
    total_sum = likes_comments['likes'] + likes_comments['comments']
    print(f'{username}: {total_sum}')
