class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        soln = [[]]

        for num in nums:
            temp = []
            for s in soln:
                temp.append(s + [num])
            soln.extend(temp)

        return soln


s = Solution()
print(s.subsets([1, 2, 3]))
