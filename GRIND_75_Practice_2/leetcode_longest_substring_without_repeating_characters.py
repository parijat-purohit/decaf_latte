class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len = 0
        l, r = 0, 0
        seen = {}

        for r, ch in enumerate(s):
            if ch in seen:
                l = max(seen[ch] + 1, l)
            seen[ch] = r
            len = max(len, r - l + 1)
        return len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
