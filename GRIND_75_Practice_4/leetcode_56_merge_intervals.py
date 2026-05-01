class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output


s = Solution()
print(s.merge([[2, 6], [8, 10], [1, 3], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
