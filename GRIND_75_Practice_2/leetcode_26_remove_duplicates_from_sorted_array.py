class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, n = 0, 0, len(nums)
        curr = None
        while j < n:
            if nums[j] != curr:
                nums[i] = nums[j]
                curr = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        nums[i:n] = '_'

        return i


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
