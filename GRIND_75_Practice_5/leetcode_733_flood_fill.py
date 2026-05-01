"""
Leetcode 733: Flood Fill
Time Complexity: O(m x n)
Space Complexity: O(m x n) Due to recursion depth in worst case it could be same as the dimension of the matrix

"""


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if old_color == color:
            return image
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] == color or image[r][c] != old_color:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)

        return image


s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
