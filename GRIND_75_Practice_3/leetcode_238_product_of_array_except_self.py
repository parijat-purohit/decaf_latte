class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1]*len(nums)

        for i in range(1, n):
            output[i] = output[i-1]*nums[i-1]

        mul = 1

        for i in range(n-1, -1, -1):
            output[i] *= mul
            mul *= nums[i]

        return output


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
