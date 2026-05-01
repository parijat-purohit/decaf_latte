"""
Leetcode 169: Majority Element
WIth Boyer Moore algorithm we achieved O(1) space complexity along with O(1) time complexity.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele, freq = None, 0

        for num in nums:
            if num != maj_ele:
                if freq == 0:
                    maj_ele = num
                    freq = 1
                else:
                    freq -= 1
            else:
                freq += 1

        return maj_ele


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
