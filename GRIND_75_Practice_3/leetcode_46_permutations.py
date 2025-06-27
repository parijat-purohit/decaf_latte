class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def dfs(i):
            if i == n:
                return res.append(nums[:])
            for j in range(i+1):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res


s = Solution()
print(s.permute([1, 2, 3, 4]))
