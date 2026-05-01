from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(mat), len(mat[0])
        queue = deque([])

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    mat[r][c] = float('inf')
                else:
                    queue.append((r, c))

        while queue:
            row, col = queue.popleft()
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dir_r, dir_c in dirs:
                new_r, new_c = row + dir_r, col + dir_c
                if 0 <= new_r < rows and 0 <= new_c < cols and mat[row][col] + 1 < mat[new_r][new_c]:
                    mat[new_r][new_c] = mat[row][col] + 1
                    queue.append((new_r, new_c))

        return mat


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
