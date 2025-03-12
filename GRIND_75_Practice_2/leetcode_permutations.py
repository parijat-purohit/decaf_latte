class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def dfs(start):
            if start == n:
                res.append(nums[:])
            else:
                for i in range(start, n):
                    nums[i], nums[start] = nums[start], nums[i]
                    dfs(start+1)
                    nums[i], nums[start] = nums[start], nums[i]
        dfs(0)
        return res


s = Solution()
print(s.permute([1, 2, 3]))
