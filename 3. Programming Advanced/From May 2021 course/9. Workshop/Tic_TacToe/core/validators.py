from Tic_TacToe.core.constants import position_mapper


def is_position_in_range(position):
    if 1 <= position <= 9:
        return True
    return False


def is_place_available(board, position):
    row, col = position_mapper[position]
    if not board[row][col] == " ":
        return False
    return True
