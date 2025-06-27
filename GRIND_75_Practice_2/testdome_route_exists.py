def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    rows = len(map_matrix)
    cols = len(map_matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if not map_matrix[r][c] or visited[r][c]:
            return False
        if r == to_row and c == to_column:
            return True

        visited[r][c] = True  # mark current cell as visited

        # Explore all 4 directions: up, down, left, right
        return (
            dfs(r + 1, c) or
            dfs(r - 1, c) or
            dfs(r, c + 1) or
            dfs(r, c - 1)
        )

    return dfs(from_row, from_column)


if __name__ == '__main__':
    map_matrix = [
        [True, True, False],
        [False, False, False],
        [True, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))
