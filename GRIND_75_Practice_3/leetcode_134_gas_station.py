class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        st_index = 0
        total_cost = 0
        for i in range(len(gas)):
            total_cost += gas[i] - cost[i]
            if total_cost < 0:
                st_index = i+1
                total_cost = 0
        return st_index


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
