deck = input().split(', ')
commands_number = int(input())

for _ in range(commands_number):
    command = input().split(', ')
    action = command[0]

    if action == 'Add':
        card_name = command[1]
        if card_name not in deck:
            deck.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif action == 'Remove':
        card_name = command[1]
        if card_name in deck:
            card_index = deck.index(card_name)
            del deck[card_index]
            print("Card successfully removed")
        else:
            print("Card not found")


    elif action == 'Remove At':
        index = int(command[1])
        if index in range(len(deck)):
            del deck[index]
            print("Card successfully removed")
        else:
            print("Index out of range")


    elif action == 'Insert':
        index = int(command[1])
        card_name = command[2]

        if index in range(len(deck)):
            if card_name in deck:
                print("Card is already added")
            else:
                deck.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(deck))
