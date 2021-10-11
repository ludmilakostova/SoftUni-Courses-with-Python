from Tic_TacToe.core.validators import is_position_in_range, is_place_available
from Tic_TacToe.core.helpers import get_row_col, print_current_board_state, is_winner, is_board_full


def play(players, board, mapper):
    # To check in range, to check if place is available
    # To check if there is a winner

    current_turn_count = 1
    while True:
        current_player = mapper[current_turn_count % 2]
        position = int(input(f'{current_player} choose a free position [1-9]: '))
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player]
                print_current_board_state(board)
                if is_winner(board):
                    print(f'{current_player} wins !')
                    exit(0)
                if is_board_full(board):
                    print(f'Game over ! No winner !')
                    exit(0)
            else:
                print(f"Please try again {current_player} by selecting an available place on the board")
                current_turn_count -= 1
        else:
            print(f"Please try again {current_player} with an number in range [1-9]")
            current_turn_count -= 1

        current_turn_count += 1


