from collections import defaultdict


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        hash_dict = defaultdict(set)
        answer = [[], []]
        for n in nums1:
            hash_dict[n].add(0)

        for n in nums2:
            hash_dict[n].add(1)

        for key, values in hash_dict.items():
            if len(values) == 1:
                answer[values.pop()].append(key)
        return answer


s = Solution()
print(s.findDifference([1, 2, 3], [2, 4, 6]))
print(s.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
