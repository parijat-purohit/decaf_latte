"""
Leetcode 278: First Bad Version

The intuitive solution is not executable due to an external dependency on third party call.
Analysis of time complexity is dependent on Binary Search algorithm.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low < high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


s = Solution()
print(s.firstBadVersion(5))
print(s.firstBadVersion(10))
