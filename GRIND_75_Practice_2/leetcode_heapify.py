import heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_store = []
        for p in points:
            dist = (p[0]**2 + p[1]**2)
            heapq.heappush(heap_store, [-dist, p])

            if len(heap_store) > k:
                heapq.heappop(heap_store)

        return [p for _, p in heap_store]


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [0, 2]], 2))
