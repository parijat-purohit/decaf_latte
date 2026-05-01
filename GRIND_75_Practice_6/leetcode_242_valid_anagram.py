"""
leetcode 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Time Complexity: O(n)
Space Complexity: O(n)

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # The dict data structure will support beyond lowercase English letters.
        ch_map = {}

        for st in s:
            ch_map[st] = ch_map.get(st, 0) + 1

        for st in t:
            if st not in ch_map:
                return False
            ch_map[st] -= 1
            if ch_map[st] < 0:
                return False
        return True


s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
print(s.isAnagram('stop', 'top'))
