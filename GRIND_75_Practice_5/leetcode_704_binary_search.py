"""
Leetcode 704: Binary Search
Time Complexity: O(log2 N)
Space Complexity: O(1)

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
