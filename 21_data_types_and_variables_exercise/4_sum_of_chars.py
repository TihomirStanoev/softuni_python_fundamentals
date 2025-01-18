chars = int(input())


character_sum = 0
for codes in range(chars):
    character = input()
    character_sum += ord(character)

print(f'The sum equals: {character_sum}')

