from Connect_Four_Game.Core.validators import direction_mapper, is_in_range_row, is_in_range_col


def print_current_state_board(board):
    [print(row) for row in board]


def is_winner(row, col, board):
    symbol = board[row][col]
    is_won = False
    for direction in direction_mapper:
        move = 0
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]
        while is_in_range_row(new_row) and is_in_range_col(new_col):
            if symbol == board[new_row][new_col] and symbol != 0:
                new_row += direction_mapper[direction][0]
                new_col += direction_mapper[direction][1]
                move += 1
                if move == 3:
                    is_won = True
                    break
            else:
                break
        if is_won:
            break
    return is_won


def is_board_full(board):
    is_full = True
    for row in board:
        if 0 in row:
            is_full = False
            break
    return is_full








