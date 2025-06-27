class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}

        for num in nums:
            if map.get(num):
                return True
            else:
                map[num] = 1
        return False


# One liner solution


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(set(nums)) != len(nums)


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4]))
