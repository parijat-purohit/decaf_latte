class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            temp = []
            for r in res:
                temp.append(r+[num])
            res.extend(temp)
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
