class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        min = 101
        for i in range(len(cost)):
            if cost[i] < min:
                min = cost[i]
            cost[i] = min

        return cost


s = Solution()
print(s.minCosts([5, 3, 4, 1, 3, 2]))
