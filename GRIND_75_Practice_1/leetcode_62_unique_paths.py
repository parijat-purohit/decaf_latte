# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         path = [[0 for _ in range(n)] for _ in range(m)]

#         def dfs(r, c):
#             if r == m-1 and c == n-1:
#                 return 1
#             elif r < 0 or c < 0 or r >= m or c >= n:
#                 return 0
#             elif path[r][c] != 0:
#                 return path[r][c]
#             else:
#                 path[r][c] = dfs(r+1, c) + dfs(r, c+1)
#                 return path[r][c]
#         return dfs(0, 0)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            path[r][0] = 1
        for c in range(n):
            path[0][c] = 1
        for r in range(1, m):
            for c in range(1, n):
                path[r][c] = path[r-1][c] + path[r][c-1]
        return path[-1][-1]


s = Solution()
print(s.uniquePaths(3, 7))
