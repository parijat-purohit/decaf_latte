class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            temp = 0
            if height[l] < height[r]:
                temp = height[l] * (r - l)
                l += 1
            else:
                temp = height[r] * (r - l)
                r -= 1
            res = max(res, temp)

        return res


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
