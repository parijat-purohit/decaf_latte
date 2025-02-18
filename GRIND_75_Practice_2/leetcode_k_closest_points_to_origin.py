import heapq


# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]


# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         heap_elements = []

#         for point in points:
#             dist = point[0]**2 + point[1]**2
#             heap_elements.append([dist, point])

#         heapq.heapify(heap_elements)

#         result = []
#         while k > 0:
#             _, point = heapq.heappop(heap_elements)
#             result.append(point)
#             k -= 1
#         return result

# Time Complexity: O(nlogk)
# Space Complexity: O(k)
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_elements = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap_elements, [-dist, point])
            if len(heap_elements) > k:
                heapq.heappop(heap_elements)

        return [p for _, p in heap_elements]


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
