class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, c = len(matrix), len(matrix[0])
        print(r, c)
        left, up, right, down = 0, 0, 0, 0


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
