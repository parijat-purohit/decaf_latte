class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]

        postfix = 1
        for i in range(n-2, -1, -1):
            prefix[i] *= postfix * nums[i+1]
            postfix *= nums[i+1]

        return prefix


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
