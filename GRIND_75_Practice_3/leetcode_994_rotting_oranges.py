from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        counter_fresh, time_elapsed = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    counter_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        if counter_fresh == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                dir_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dir_r, dir_c in dir_map:
                    new_r, new_c = r+dir_r, c+dir_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        counter_fresh -= 1
            time_elapsed += 1
        return time_elapsed - 1 if counter_fresh == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
