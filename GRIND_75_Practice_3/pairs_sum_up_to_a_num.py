class Solution():
    def sumup(self, nums, target):
        seen = set()
        res = []

        for num in nums:
            if target - num in seen:
                res.append((num, target-num))
            seen.add(num)
        return res


s = Solution()
print(s.sumup([2, 3, 1, 4, 6, 7, 5], 9))
