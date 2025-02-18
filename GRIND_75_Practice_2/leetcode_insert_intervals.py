class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        length = len(intervals)
        start, end = newInterval
        output = []
        while (i < length and intervals[i][1] < start):
            output.append(intervals[i])
            i += 1

        while (i < length and intervals[i][0] <= end):
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        output.append([start, end])

        while (i < length):
            output.append(intervals[i])
            i += 1
        return output


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
