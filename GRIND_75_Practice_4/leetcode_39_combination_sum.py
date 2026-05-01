class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        n = len(candidates)

        def backtrack(i, arr, total):
            if total == target:
                output.append(arr[:])
                return
            if i == n or total > target:
                return
            arr.append(candidates[i])
            backtrack(i, arr, total + candidates[i])
            arr.pop()
            backtrack(i+1, arr, total)
        backtrack(0, [], 0)
        return output


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
