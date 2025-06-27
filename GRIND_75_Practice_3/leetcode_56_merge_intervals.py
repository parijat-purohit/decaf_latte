class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda interval: interval[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1] = [output[-1][0],
                              max(output[-1][1], intervals[i][1])]
            else:
                output.append(intervals[i])
        return output


s = Solution()
print(s.merge([[2, 4], [1, 2], [3, 7], [2, 5]]))
