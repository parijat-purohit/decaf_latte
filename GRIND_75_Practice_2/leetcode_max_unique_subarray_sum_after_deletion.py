class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        visited = set()
        sum = -100

        for i in range(len(nums)):
            if nums[i] not in visited:
                sum = max(nums[i], sum + nums[i], sum)
                visited.append(nums[i])
        return sum


s = Solution()
print(s.maxSum([1, 2, -1, -2, 0, 1, 0, -1]))
print(s.maxSum([1, 1, 0, 1, 1]))
print(s.maxSum([1, 2, 3, 4, 5]))
print(s.maxSum([-20, 20]))
print(s.maxSum([-100]))
print(s.maxSum([2, -10, 6]))
print(s.maxSum([-17, -15]))
