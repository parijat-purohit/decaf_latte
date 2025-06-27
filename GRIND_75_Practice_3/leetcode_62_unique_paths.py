# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         grid = [[0 for _ in range(n)] for _ in range(m)]

#         for i in range(n):
#             grid[0][i] = 1

#         for j in range(m):
#             grid[j][0] = 1

#         for r in range(1, m):
#             for c in range(1, n):
#                 grid[r][c] = grid[r-1][c] + grid[r][c-1]

#         return grid[m-1][n-1]

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        map = {}

        def dfs(m, n):
            if m == 0 or n == 0:
                return 1
            if (m, n) in map:
                return map[(m, n)]
            map[m, n] = dfs(m-1, n) + dfs(m, n-1)
            return map[m, n]
        return dfs(m-1, n-1)


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(2, 2))
print(s.uniquePaths(5, 2))
print(s.uniquePaths(2, 5))
print(s.uniquePaths(4, 3))
print(s.uniquePaths(4, 4))
print(s.uniquePaths(5, 5))
print(s.uniquePaths(6, 5))
print(s.uniquePaths(6, 4))
