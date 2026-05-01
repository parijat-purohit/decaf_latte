"""
Leetcode 1. Two Sum
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_map = {}

        for i, num in enumerate(nums):
            if target - num in sum_map:
                return [sum_map[target-num], i]
            sum_map[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
