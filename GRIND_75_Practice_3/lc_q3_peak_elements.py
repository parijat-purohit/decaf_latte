class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
            if i == len(nums) - 2:
                return i+1


s = Solution()
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(s.findPeakElement([1, 2]))
