"""
Complexity Analysis:
Time Complexity: 
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total//2
        memo = set()
        memo.add(0)

        for n in nums:
            temp = set()
            for m in memo:
                if n+m == target:
                    return True
                temp.add(n+m)
                temp.add(m)
            memo = temp
        return False
