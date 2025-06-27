class Solution(object):
    def subsets(self, nums, target):
        def backtrack(ind, path, total):
            if total == 0:
                result.append(path[:])
            if ind == len(nums):
                return

            if total - nums[ind] >= 0:
                path.append(nums[ind])
                backtrack(ind, path, total - nums[ind])
                path.pop()
                backtrack(ind+1, path, total)

        result = []
        backtrack(0, [], target)
        return result


s = Solution()
print(s.subsets([2, 3, 5, 7], 10))


class Solution(object):
    def permutation(self, nums):
        res = []

        def dfs(start):
            if start == len(nums):
                res.append(nums[:])
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        dfs(0)
        return res


s = Solution()
print(s.permutation([1, 2, 3]))
