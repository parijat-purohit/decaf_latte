"""
Leetcode 242: Valid Anagram
Time Complexity: O(max(len(s), len(t)))
Space Complexity: O(1), It's length of the character not the character is growing with increasing input size.
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

        ch_map = {}

        for st in s:
            if st not in ch_map:
                ch_map[st] = 1
            else:
                ch_map[st] += 1

        for st in t:
            if st not in ch_map or ch_map[st] == 0:
                return False
            ch_map[st] -= 1
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("cat", "rat"))
