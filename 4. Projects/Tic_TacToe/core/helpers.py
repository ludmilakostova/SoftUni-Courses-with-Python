from Tic_TacToe.core.constants import position_mapper


def get_row_col(pos):
    return position_mapper[pos]


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full


def is_row_winner(board):
    is_found = False
    for row in board:
        if row.count("X") == len(row) or row.count("0") == len(row):
            is_found = True
    return is_found


def is_col_winner(board):
    is_found = False

    first = [board[0][0], board[1][0], board[2][0]]
    second = [board[0][1], board[1][1], board[2][1]]
    third = [board[0][2], board[1][2], board[2][2]]

    if first.count("X") == len(board) or first.count("O") == len(board):
        is_found = True
    elif second.count("X") == len(board) or second.count("O") == len(board):
        is_found = True
    elif third.count("X") == len(board) or third.count("O") == len(board):
        is_found = True

    return is_found


def is_diagonal_winner(board):
    is_found = False
    primary = [board[0][0], board[1][1], board[2][2]]
    secondary = [board[0][2], board[1][1], board[2][0]]
    if primary.count("X") == len(board) or primary.count("O") == len(board):
        is_found = True
    elif secondary.count("X") == len(board) or secondary.count("O") == len(board):
        is_found = True
    return is_found


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) or is_diagonal_winner(board):
        return True
    return False

