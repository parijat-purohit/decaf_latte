class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1] = ([new_intervals[-1][0],
                                     max(new_intervals[-1][1], intervals[i][1])])
            else:
                new_intervals.append(intervals[i])
        return new_intervals


s = Solution()
print(s.merge([[2, 6], [1, 3], [4, 10], [15, 18]]))
