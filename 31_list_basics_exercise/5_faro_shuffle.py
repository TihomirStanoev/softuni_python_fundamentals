deck = input().split()
shuffles = int(input())


half = len(deck) // 2
shuffle_deck = []

for number_shuffles in range(shuffles):
    left_side = []
    right_side = []
    for card in range(half):
        left_side.append(deck[card])
        right_side.append(deck[card+half])

    shuffle_deck = []
    for shuffle_card in range(half):
        shuffle_deck.append(left_side[shuffle_card])
        shuffle_deck.append(right_side[shuffle_card])
    deck = shuffle_deck.copy()


print(shuffle_deck)

