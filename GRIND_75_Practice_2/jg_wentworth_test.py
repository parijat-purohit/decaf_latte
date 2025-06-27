def get_count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            if not matrix[i][j] and j != i+1:
                count += 1
            matrix[i][j] = True
    return count


if __name__ == "__main__":
    matrix = [
        [False, True, False, False, False],
        [True, False, False, False, False],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [False, False, False, False, False],
    ]
    print(get_count(matrix))  # should print 6
