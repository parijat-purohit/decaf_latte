class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        overlap_width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        overlap_height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])

        return True if overlap_width > 0 and overlap_height > 0 else False


s = Solution()
print(s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
print(s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))
print(s.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))
print(s.isRectangleOverlap([4, 4, 14, 7], [4, 3, 8, 8]))
