from collections import defaultdict


class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        count, sum = 0, 0
        l = 0
        r = l+1

        while l < len(capacity) - 1:
            sum = capacity[l]
            while sum > 0 and r < len(capacity):
                sum -= capacity[r]
                if sum == 0:

                r += 1


s = Solution()
print(s.countStableSubarrays([9, 3, 3, 3, 9]))
print(s.countStableSubarrays([1, 2, 3, 4, 5]))
print(s.countStableSubarrays([-4, 4, 0, 0, -8, -4]))
print(s.countStableSubarrays([0, 0, 0, 0]))
