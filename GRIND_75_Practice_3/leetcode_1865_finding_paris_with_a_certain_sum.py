from collections import Counter


class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_count = Counter(self.nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums2_count[self.nums2[index]] -= 1
        if self.nums2_count[self.nums2[index]] == 0:
            del self.nums2_count[self.nums2[index]]
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        counter = 0
        for num in self.nums1:
            if tot - num in self.nums2_count:
                print(tot - num, self.nums2_count[tot-num])
                counter += self.nums2_count[tot-num]
        return counter


f = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(f.count(7))
print(f.count(4))
f.add(0, 1)
