class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l, r = 0, 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                res = max(res, ((r-l) * height[l]))
                l += 1
            else:
                res = max(res, ((r-l)*height[r]))
                r -= 1
        return res


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
