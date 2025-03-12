class Solution(object):
    def combinationSum(self, nums, target):
        res = []

        def backtrack(temp, cur, total):
            if total == 0:
                return res.append(temp[:])

            if total < 0 or cur == len(nums):
                return

            temp.append(nums[cur])
            backtrack(temp, cur, total - nums[cur])
            temp.pop()
            backtrack(temp, cur+1, total)

        backtrack([], 0, target)
        return res


s = Solution()
print(s.combinationSum([2, 3, 5, 7, 11], 10))
