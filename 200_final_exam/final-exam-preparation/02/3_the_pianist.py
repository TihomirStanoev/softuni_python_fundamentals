def add_piece(piano_dict, piece, composer, key):
    if piece in piano_dict.keys():
        print(f"{piece} is already in the collection!")
    else:
        piano_dict[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")

    return piano_dict

def remove_piece(piano_dict, piece):
    if piece in piano_dict.keys():
        del piano_dict[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return piano_dict

def change_key(piano_dict, piece, new_key):
    if piece in piano_dict.keys():
        piano_dict[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return piano_dict

piano_pieces = dict() # {'piece': str, 'composer':str, 'key': str }
number_pieces = int(input())

for _ in range(number_pieces):
    piece_list = input().split('|')
    piece, composer, key = piece_list[0], piece_list[1], piece_list[2]
    piano_pieces[piece] = {'composer': composer, 'key': key}



while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split('|')
    action, piece = command[0], command[1]

    if action == 'Add':
        composer = command[2]
        key = command[3]
        piano_pieces = add_piece(piano_pieces, piece, composer, key)

    elif action == 'Remove':
        piano_pieces = remove_piece(piano_pieces, piece)

    elif action == 'ChangeKey':
        key = command[2]
        piano_pieces = change_key(piano_pieces, piece, key)


for piece in piano_pieces.items():
    piece_name = piece[0]
    composer_name = piece[1]['composer']
    key_name = piece[1]['key']
    print(f"{piece_name} -> Composer: {composer_name}, Key: {key_name}")

