class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, max_area = 0, len(height) - 1, 0
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, (r-l)*height[l])
                l += 1
            else:
                max_area = max(max_area, (r-l) * height[r])
                r -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
