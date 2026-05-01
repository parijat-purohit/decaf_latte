class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sq = [n**2 for n in nums]

        nums_sq.sort(reverse=True)

        nums_len = len(nums)
        sum = 0
        if nums_len % 2 == 0:
            for i in range(nums_len//2):
                sum += nums_sq[i]
            for i in range(nums_len//2, nums_len):
                sum -= nums_sq[i]
        else:
            for i in range(nums_len//2+1):
                sum += nums_sq[i]
            for i in range(nums_len//2+1, nums_len):
                sum -= nums_sq[i]

        return sum


s = Solution()
print(s.maxAlternatingSum([1, -1, 2, -2, 3, -3]))
print(s.maxAlternatingSum([1, 2, 3]))
