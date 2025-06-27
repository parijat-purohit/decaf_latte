from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque([])
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            r, c = queue.popleft()
            dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dir_r, dir_c in dir:
                new_r, new_c = r + dir_r, c + dir_c
                if 0 <= new_r < rows and 0 <= new_c < cols and mat[r][c] + 1 < mat[new_r][new_c]:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))

        return mat


s = Solution()

print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
