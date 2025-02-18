from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    mat[r][c] = float('inf')
                else:
                    queue.append([r, c])

        dir_map = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for d_r, d_c in dir_map:
                new_dr, new_dc = r + d_r, c + d_c
                if (0 <= new_dr < rows and 0 <= new_dc < cols and
                        mat[new_dr][new_dc] > mat[r][c] + 1):
                    mat[new_dr][new_dc] = mat[r][c] + 1
                    queue.append([new_dr, new_dc])
        return mat


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
