class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        prefix = [1]*len_nums

        for i in range(1, len_nums):
            prefix[i] = prefix[i-1]*nums[i-1]

        mul = 1

        for i in range(len_nums-1, -1, -1):
            prefix[i] = prefix[i] * mul
            mul *= nums[i]

        return prefix


s = Solution()
print(s.productExceptSelf([2, 3, 4, 5]))
