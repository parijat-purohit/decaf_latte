class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        first, last, d = None, None, 0

        for i, s in enumerate(seats):
            if s:
                if first is None:
                    first = i
                if last is not None:
                    d = max(d, i - last)
                last = i
        return max(first, len(seats) - 1 - last, d//2)


s = Solution()
print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
