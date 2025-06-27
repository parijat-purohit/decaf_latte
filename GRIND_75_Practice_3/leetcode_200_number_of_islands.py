class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            grid[i][j] = "0"
            dir_map = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for r, c in dir_map:
                new_r, new_c = i + r, j + c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)
        return counter


s = Solution()
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
