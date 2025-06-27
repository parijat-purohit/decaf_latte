class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            left += 1
        return output


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
