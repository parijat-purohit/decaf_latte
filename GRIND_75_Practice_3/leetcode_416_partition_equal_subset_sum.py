class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total % 2 != 0 or len(nums) == 1:
            return False

        total = total//2

        memo = set()
        memo.add(0)

        for num in nums:
            temp = set()
            for m in memo:
                if num + m == total:
                    return True
                if num+m < total:
                    temp.add(num+m)
                temp.add(m)
            memo = temp
        return False


s = Solution()
print(s.canPartition([1, 2, 5]))
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))
print(s.canPartition([1, 3, 4, 4]))
