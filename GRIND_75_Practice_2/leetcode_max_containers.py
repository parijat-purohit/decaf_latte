class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        num_grids = n**2
        total_weight = 0
        total_grid = 0
        for _ in range(num_grids):
            if total_weight <= maxWeight and total_grid <= num_grids:
                total_weight += w
                total_grid += 1
            else:
                break

        if total_weight > maxWeight:
            total_grid -= 1

        return total_grid


s = Solution()
print(s.maxContainers(2, 3, 15))
print(s.maxContainers(3, 5, 20))
print(s.maxContainers(3, 4, 66))
