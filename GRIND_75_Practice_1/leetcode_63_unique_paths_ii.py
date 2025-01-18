class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for r in range(1, rows):
            if obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = obstacleGrid[r-1][0]

        for c in range(1, cols):
            if obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
            else:
                obstacleGrid[0][c] = obstacleGrid[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + \
                        obstacleGrid[r][c-1]

        return obstacleGrid[-1][-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
