sheeps = input()

sheeps_list = sheeps.split(", ")
l = len(sheeps_list) - 1

for i, w in enumerate(sheeps_list):
    if 'wolf' == w:
        if i == l:
            print("Please go away and stop eating my sheep")
    if 'wolf' == w and i != l:
        print(f'Oi! Sheep number {l - i}! You are about to be eaten by a wolf!')
