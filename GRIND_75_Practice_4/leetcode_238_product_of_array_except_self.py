class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        mul = 1

        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            output[i] = mul * output[i]
            mul *= nums[i]

        return output


s = Solution()
print(s.productExceptSelf([2, 3, 4, 5]))
