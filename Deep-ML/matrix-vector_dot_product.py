def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    row_length = len(a)
    col_length = len(a[0])
    vec_length = len(b)

    if col_length != vec_length:
        return -1
    else:
        mul_res = []
        for r in range(row_length):
            temp = 0
            for c in range(col_length):
                temp += (a[r][c]*b[c])
            mul_res.append(temp)
    return mul_res


print(matrix_dot_vector([[1, 2], [2, 4]], [1, 2]))
