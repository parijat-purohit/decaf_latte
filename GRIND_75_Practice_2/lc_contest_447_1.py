from collections import defaultdict


class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        x_map = defaultdict(list)
        y_map = defaultdict(list)

        for x, y in buildings:
            x_map[x].append(y)
            y_map[y].append(x)

        for entry in x_map.values():
            entry.sort()

        for entry in y_map.values():
            entry.sort()

        count = 0
        for x, y in buildings:
            if (x_map[x][0] != y and x_map[x][-1] != y and
                    y_map[y][0] != x and y_map[y][-1] != x):
                count += 1

        return count


s = Solution()
print(s.countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(s.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]))
print(s.countCoveredBuildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]))
