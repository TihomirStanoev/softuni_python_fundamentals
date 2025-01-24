deck = input()
count = int(input())

deck = deck.split(' ')

faro_deck = deck.copy()


half = len(deck) // 2

for _ in range(count):
    for card in range(half):
        if card > 0:
            faro_deck[card * 2] = deck[card]

    pos = 0
    for card in range(len(deck) - 1):
        if card % 2 == 0:
            continue
        faro_deck[card] = deck[half + pos]
        pos += 1

    deck = faro_deck

print(faro_deck)
