def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    len_row = len(a)
    len_col = len(a[0])

    res = []
    for r in range(len_col):
        temp = []
        for c in range(len_row):
            temp.append(a[c][r])
        res.append(temp)
    return res


print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
