class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        seen = {}
        length = 0

        for r, ch in enumerate(s):
            if ch in seen:
                l = max(seen[ch] + 1, l)
            seen[ch] = r
            length = max(length, r - l + 1)
        return length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
