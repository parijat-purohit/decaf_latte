def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    rows = len(game_matrix)
    cols = len(game_matrix[0])

    if (to_row >= rows or
        to_column >= cols or
        from_row >= rows or
            from_column >= cols):
        return False

    if from_column != to_column:
        for i in range(from_column, to_column+1):
            if not game_matrix[i][from_row]:
                return False

    if from_row != to_row:
        for j in range(from_row, to_row + 1):
            if not game_matrix[from_column][j]:
                return False

    return True


if __name__ == "__main__":
    game_matrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(game_matrix, 3, 2, 2, 2))  # True, Valid move
    # False, Can't travel through land
    print(can_travel_to(game_matrix, 3, 2, 3, 4))
    print(can_travel_to(game_matrix, 3, 2, 6, 2))  # False, Out of bounds
