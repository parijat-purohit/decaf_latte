class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        sorted(events, key=lambda x: x[0])

        output = [events[0]]

        for i in range(1, len(events)):
            if events[i][0] <= output[-1][1]:
                min_int = min(events[i][0], output[-1][0])
                max_int = max(events[i][1], output[-1][1])
                output[-1] = [min_int, max_int]
            else:
                output.append(events[i])

        return output


s = Solution()
print(s.maxEvents([[1, 4], [2, 5], [7, 8]]))
