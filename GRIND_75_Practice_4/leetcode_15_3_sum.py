class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        i = 0
        n = len(nums)
        while (i < n-2):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j, k = i+1, n-1

            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif t > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return output


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 0, 0]))
