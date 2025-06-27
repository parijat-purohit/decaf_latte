class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        l, length = 0, 0
        for r, ch in enumerate(s):
            if ch in seen:
                l = max(l, seen[ch]+1)
            length = max(length, r - l + 1)
            seen[ch] = r

        return length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
