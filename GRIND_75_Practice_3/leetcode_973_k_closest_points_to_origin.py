import heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_elements = []

        for point in points:
            heapq.heappush(
                heap_elements, [-(point[0]*point[0] + point[1]*point[1]), point])
            if len(heap_elements) > k:
                heapq.heappop(heap_elements)

        return [point for _, point in heap_elements]


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
