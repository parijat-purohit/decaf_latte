class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for _ in range(n)] for _ in range(n)]
        left, up, right, down = 0, 0, n-1, n-1
        num = 1
        while left <= right and up <= down:
            for i in range(left, right+1):
                mat[up][i] = num
                num += 1
            up += 1
            for i in range(up, down+1):
                mat[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                mat[down][i] = num
                num += 1
            down -= 1
            for i in range(down, up-1, -1):
                mat[i][left] = num
                num += 1
            left += 1
        return mat


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(4))
