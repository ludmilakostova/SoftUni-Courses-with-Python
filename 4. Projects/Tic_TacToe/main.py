from core.logic import play


def print_initial_board_positions():
    print("This is the numeration of the board:")
    print(f'| 1 | 2 | 3|')
    print(f'| 4 | 5 | 6|')
    print(f'| 7 | 8 | 9|')


def create_empty_board():
    return [[" ", " ", " "]for _ in range(3)]


def setup():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    player_1_sign = input(f'{player_1} would you like to play with X or O? ').upper()
    while not player_1_sign in ["X", "O"]:
        player_1_sign = input(f'{player_1} would you like to play with X or O? ')

    player_2_sign = "O" if player_1_sign == "X" else "X"

    print_initial_board_positions()
    print(f'{player_1} starts first!')
    board = create_empty_board()

    players = {player_1: player_1_sign, player_2: player_2_sign}
    turns_mapper = {0: player_2, 1: player_1}
    play(players, board, turns_mapper)


def start_game():
    setup()


if __name__ == "__main__":
    start_game()
