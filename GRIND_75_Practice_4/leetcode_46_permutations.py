class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output, sol = [], []

        def dfs():
            if len(sol) == n:
                output.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    dfs()
                    sol.pop()

        dfs()
        return output


s = Solution()
print(s.permute([1, 2, 3]))
