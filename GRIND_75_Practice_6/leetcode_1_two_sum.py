"""
Leetcode 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

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
        ind_map = {}

        for i, num in enumerate(nums):
            if target - num in ind_map:
                return [ind_map[target-num], i]
            ind_map[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
