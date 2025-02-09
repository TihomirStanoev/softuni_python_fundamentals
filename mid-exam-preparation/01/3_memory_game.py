def add_a(number, tw_list):
    [tw_list.insert(len(tw_list)//2, str(-number)+'a') for _ in range(2)]
    return 'Invalid input! Adding additional elements to the board'

def maching_elements(small_index, second_index, tw_list):
    mached = tw_list.pop(small_index)
    tw_list.pop(second_index-1)

    return f'Congrats! You have found matching elements - {mached}!'


twin_list = list(input().split())


moves = 0
while True:
    if not twin_list:
        print(f'You have won in {moves} turns!')
        break

    command = input()
    if command == 'end':
        print(f'Sorry you lose :(')
        print(' '.join(str(_) for _ in twin_list))
        break

    command_list = list(map(int, command.split()))
    command_list.sort()
    small, big = command_list

    moves += 1

    if small not in range(0, len(twin_list)) or big not in range(0, len(twin_list)) or small == big:
        print(add_a(moves, twin_list))
        continue

    if twin_list[small] == twin_list[big]:
        print(maching_elements(small,big,twin_list))
    else:
        print('Try again!')
