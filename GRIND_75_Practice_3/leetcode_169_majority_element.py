# solving using Boyer-Moore voting algorithm.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)

        return res


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
