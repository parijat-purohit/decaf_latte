class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1, r2 = 0, 0

        for num in nums:
            temp = max(num + r1, r2)
            r1 = r2
            r2 = temp
        return r2


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 3, 9, 7, 1]))
