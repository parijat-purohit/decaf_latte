from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten_orange_tracker = deque([])
        fresh_orange_count = 0
        time_counter = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_orange_tracker.append((r, c))
                if grid[r][c] == 1:
                    fresh_orange_count += 1

        dir_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while (rotten_orange_tracker and fresh_orange_count > 0):
            len_queue = len(rotten_orange_tracker)
            for _ in range(len_queue):
                row, col = rotten_orange_tracker.popleft()
                for dir_r, dir_c in dir_map:
                    new_r, new_c = row + dir_r, col + dir_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        rotten_orange_tracker.append((new_r, new_c))
                        fresh_orange_count -= 1
            time_counter += 1

        return time_counter if fresh_orange_count == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[0]]))
