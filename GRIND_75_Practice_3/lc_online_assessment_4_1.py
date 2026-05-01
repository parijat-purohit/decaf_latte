class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        seat_distance = [0] * n
        for i in range(1, n):
            if seats[i] == 1:
                seat_distance[i] = 0
            else:
                seat_distance[i] = seat_distance[i-1] + 1

        for i in range(n-2, -1, -1):
            if seat_distance[i] != 0:
                seat_distance[i] = min(
                    seat_distance[i], seat_distance[i+1] + 1)

        return max(seat_distance)


s = Solution()
print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
print(s.maxDistToClosest([1, 0, 0, 0]))
