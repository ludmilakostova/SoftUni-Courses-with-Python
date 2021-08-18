number_pieces = int(input())
pieces = {}
for i in range(number_pieces):
    piece, composer, key = input().split("|")
    if piece not in pieces:
        pieces[piece] = {"composer": composer, "key": key}

command = input()
while not command == "Stop":
    instruction = command.split("|")
    action = instruction[0]
    piece = instruction[1]
    if action == "Add":
        composer = instruction[2]
        key = instruction[3]
        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif action == "ChangeKey":
        new_key = instruction[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"]))
for piece, data in sorted_pieces:
    print(f'{piece} -> Composer: {data["composer"]}, Key: {data["key"]}')
