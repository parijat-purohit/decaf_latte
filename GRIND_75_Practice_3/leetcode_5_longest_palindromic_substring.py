class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx, max_len = 0, 0
        str_length = len(s)

        for i in range(str_length):
            # check odd length
            l, r = i, i

            while l >= 0 and r < str_length and s[l] == s[r]:
                if r-l+1 > max_len:
                    idx = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # check even length
            l, r = i, i+1

            while l >= 0 and r < str_length and s[l] == s[r]:
                if r-l+1 > max_len:
                    idx = l
                    max_len = r - l + 1
                l -= 1
                r += 1
        return s[idx: idx+max_len]


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("ccc"))
