class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(i, arr, sum):
            if sum == target:
                res.append(arr[:])
                return
            if i == len(candidates) or sum > target:
                return
            arr.append(candidates[i])
            backtrack(i, arr, sum + candidates[i])
            arr.pop()
            backtrack(i+1, arr, sum)

        backtrack(0, [], 0)
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
