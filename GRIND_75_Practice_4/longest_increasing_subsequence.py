class solution(object):
    def LIS(self, nums):
        n = len(nums)
        dp = [1]*n

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)

        print(dp)
        return dp[-1]


s = solution()
print(s.LIS([1, 4, 3, 2, 8]))
