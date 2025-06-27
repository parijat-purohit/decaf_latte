class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = nums[0]
        for i in range(1, len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
