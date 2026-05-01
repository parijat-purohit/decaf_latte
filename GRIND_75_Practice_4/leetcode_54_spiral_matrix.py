class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        left, up, right, down = 0, 0, cols - 1, rows - 1
        output = []

        while left <= right and up <= down:
            i = left
            while i <= right and up <= down:
                output.append(matrix[up][i])
                i += 1
            up += 1

            i = up
            while i <= down and left <= right:
                output.append(matrix[i][right])
                i += 1
            right -= 1

            i = right
            while i >= left and up <= down:
                output.append(matrix[down][i])
                i -= 1
            down -= 1

            i = down
            while i >= up and left <= right:
                output.append(matrix[i][left])
                i -= 1
            left += 1

        return output


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
