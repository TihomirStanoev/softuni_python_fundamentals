players = input()

players_list = players.split(' ') # ['A-1', 'A-5', 'A-10', 'B-2']
players_list = list(set(players_list))


count_team_a = 11
count_team_b = 11
terminated = False

for team_player in players_list:
    if team_player[0] == "A":
        count_team_a -= 1
    elif team_player[0] == "B":
        count_team_b -= 1
    if count_team_a < 7 or count_team_b < 7:
        terminated = True
        break

print(f'Team A - {count_team_a}; Team B - {count_team_b}')

if terminated:
    print("Game was terminated")