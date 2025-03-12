from heapq import heappush, heappop


class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*len(nums1)
        temp = []

        # for i in range(len(nums1)):
        #     for j in range(len(nums1)):
        #         if nums1[j] < nums1[i]:
        #             temp.append(nums2[j])
        #     res[i] = temp
        #     temp = []

        # for i in range(len(res)):
        #     if len(res[i]) <= k:
        #         res[i] = sum(res[i])
        #     else:
        #         top_k = sorted(res[i], reverse=True)[:k]
        #         res[i] = sum(top_k)

        # return res
        n = len(nums1)
        pairs = [(nums1[i], nums2[i], i) for i in range(n)]
        print(pairs)
        pairs.sort()
        print(pairs)


s = Solution()
print(s.findMaxSum([4, 2, 1, 5, 3], [10, 20, 30, 40, 50], 2))
