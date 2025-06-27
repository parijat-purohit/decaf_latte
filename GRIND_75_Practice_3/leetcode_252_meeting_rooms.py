class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True


i1 = Interval(0, 30)
i2 = Interval(5, 10)
i3 = Interval(15, 20)
i4 = Interval(5, 8)
i5 = Interval(9, 15)

s = Solution()
print(s.canAttendMeetings([i1, i3, i2]))
print(s.canAttendMeetings([i4, i5]))
