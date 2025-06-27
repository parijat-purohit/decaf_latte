class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def dfs(ind):
            if ind >= len(nums):
                return 0
            if ind in memo:
                return memo[ind]
            memo[ind] = max((nums[ind] + dfs(ind+2)), dfs(ind+1))
            return memo[ind]
        return dfs(0)


s = Solution()
print(s.rob([2, 7, 9, 6]))
