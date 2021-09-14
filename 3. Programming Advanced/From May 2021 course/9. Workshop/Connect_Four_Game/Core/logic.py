from Connect_Four_Game.Core.validators import is_in_range_col, is_in_range_row, position_mapper
from Connect_Four_Game.Core.helpers import print_current_state_board, is_winner, is_board_full


def play(players, board, mapper):
    current_turn_count = 1

    while True:
        current_player = mapper[current_turn_count % 2]
        position_col = int(input(f'{current_player}, please choose a column in range [1-7]' ))
        try:
            position_col = position_mapper[position_col]
        except KeyError:
            print(f'Selected column out of range!')
            continue

        if is_in_range_col(position_col):
            position_row = len(board) - 1
            try:
                while board[position_row][position_col] != 0:
                    position_row -= 1
            except IndexError:
                pass
            if is_in_range_row(position_row):
                board[position_row][position_col] = players[current_player]
                print_current_state_board(board)
                if is_winner(position_row, position_col, board):
                    print(f'{current_player} wins !')
                    exit(0)
                if is_board_full(board):
                    print(f' The board is full ! Game over ! No winners')
                    exit(0)
            else:
                print(f'{current_player}, no more space in this column!')
                current_turn_count -= 1
        else:
            print(f'{current_player}, please select a column in the range [1-9]!')
            current_turn_count -= 1

        current_turn_count += 1
