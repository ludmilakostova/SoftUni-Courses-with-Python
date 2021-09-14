from Connect_Four_Game.Core.logic import play


def print_initial_board():
    board = []
    for row in range(6):
        board.append([0] * 7)

    for row in board:
        print(row)

    return board


def setup():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    player_1_sign = 1
    player_2_sign = 2
    print(f'{player_1}, your sign is {player_1_sign}')
    print(f'{player_2}, your sign is {player_2_sign}')
    print(f'{player_1}, {player_2}, the game starts now. Let\'s connect 4 consecutive slots.')

    board = print_initial_board()

    players = {player_1: player_1_sign, player_2: player_2_sign}
    turns_mapper = {0: player_2, 1: player_1}

    play(players, board, turns_mapper)


def start_game():
    setup()


if __name__ == "__main__":
    start_game()
