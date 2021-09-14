position_mapper = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6
}


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "d_left_up": (-1, -1),
    "d_right_up": (-1, 1),
    "d_left_down": (1, -1),
    "d_right_down": (1, 1)
}


def is_in_range_col(position):
    if 0 <= position < 7:
        return True
    return False


def is_in_range_row(row):
    if 0 <= row < 6:
        return True
    return False


