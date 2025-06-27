class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        output = []
        i = 0
        length = len(intervals)

        while i < length and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < length and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        output.append(newInterval)

        while i < length:
            output.append(intervals[i])
            i += 1

        return output


s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
