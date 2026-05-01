class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    curr = nums[i]
                    cnt += 1
        return curr


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
