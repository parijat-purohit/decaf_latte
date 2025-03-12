class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        no_of_islands = 0
        dir_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            grid[row][col] = '0'
            for dir_r, dir_c in dir_map:
                new_row, new_col = row + dir_r, col + dir_c
                if (new_row >= 0 and new_col >= 0 and new_row < rows and new_col < cols
                        and grid[new_row][new_col] == '1'):
                    dfs(new_row, new_col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    no_of_islands += 1
                    dfs(r, c)
        return no_of_islands


s = Solution()
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
