class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, top, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1
        output = []
        while left <= right and top <= bottom:
            i = left
            while i <= right and top <= bottom:
                output.append(matrix[top][i])
                i += 1
            top += 1
            i = top
            while i <= bottom and left <= right:
                output.append(matrix[i][right])
                i += 1
            right -= 1
            i = right
            while i >= left and top <= bottom:
                output.append(matrix[bottom][i])
                i -= 1
            bottom -= 1
            i = bottom
            while i >= top and left <= right:
                output.append(matrix[i][left])
                i -= 1
            left += 1
        return output


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
