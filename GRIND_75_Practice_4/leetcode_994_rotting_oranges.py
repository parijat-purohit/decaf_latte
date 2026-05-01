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
        fresh_count, time_elapsed = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if fresh_count == 0:
            return 0

        while queue:
            for _ in range(len(queue)):
                cur_row, cur_col = queue.popleft()
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dir_r, dir_c in dirs:
                    new_r, new_c = cur_row + dir_r, cur_col + dir_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        fresh_count -= 1
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
            time_elapsed += 1

        return time_elapsed-1 if fresh_count == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting([[0, 2]]))
