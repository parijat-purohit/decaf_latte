from collections import deque

# BFS


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque([])
        fresh, time = 0, 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        while fresh > 0 and queue:
            len_queue = len(queue)
            while len_queue > 0:
                r, c = queue.popleft()
                len_queue -= 1
                dir_map = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dir_r, dir_c in dir_map:
                    new_r, new_c = r + dir_r, c + dir_c
                    if (new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols and
                            grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
