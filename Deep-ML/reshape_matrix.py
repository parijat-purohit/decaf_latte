def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
    len_row = len(a)
    len_col = len(a[0])

    if new_shape[0] * new_shape[1] != len_row * len_col:
        return []

    res = []
    old_row = 0
    old_col = 0
    for _ in range(new_shape[0]):
        temp = []
        for _ in range(new_shape[1]):
            temp.append(a[old_row][old_col])
            old_col += 1
            if old_col == len_col:
                old_row += 1
                old_col = 0
        res.append(temp)
    return res


print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))
