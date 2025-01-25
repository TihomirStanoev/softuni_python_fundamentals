deck = ['ace', 'two', 'three', 'four', 'five', 'six']  # input().split()
shuffles = 1



half = len(deck) // 2
fc = 1
shuffle_deck = []

for shuffle in range(3):
    shuffle_deck.append(deck[half])
    half += 1
    shuffle_deck.append(deck[fc])
    fc += 1



print(half)



