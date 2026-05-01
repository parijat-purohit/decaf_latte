class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_sum, global_sum = -float('inf'), -float('inf')
        for num in nums:
            local_sum = max(local_sum + num, num)
            global_sum = max(global_sum, local_sum)

        return global_sum


s = Solution()
print(s.maxSubArray([5, 4, -1, 7, 8]))
print(s.maxSubArray([-1]))
