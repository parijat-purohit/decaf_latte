class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        total_islands = 0

        def dfs(row, col):
            grid[row][col] = '0'
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dir_r, dir_c in dirs:
                new_r, new_c = row + dir_r, col + dir_c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    total_islands += 1
                    dfs(r, c)

        return total_islands


s = Solution()
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
