class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(n):
            grid[0][r] = 1
        for c in range(m):
            grid[c][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]


s = Solution()
print(s.uniquePaths(3, 7))
