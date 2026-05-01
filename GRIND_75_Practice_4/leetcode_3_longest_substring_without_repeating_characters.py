class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, max_len = 0, 0
        seen = {}

        for r, ch in enumerate(s):
            if ch in seen:
                l = max(l, seen[ch]+1)
            max_len = max(max_len, r-l+1)
            seen[ch] = r

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
