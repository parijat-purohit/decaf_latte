class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        len_s = len(s)
        st, max_length = 0, 0

        if len_s==1:
            return s

        while i < len_s-1:
            # check even legth
            l, r = i, i

            while l >= 0 and r < len_s and s[l] == s[r]:
                if r-l+1 > max_length:
                    st, max_length = l, max(max_length, r-l+1)
                l -= 1
                r += 1

            # check odd length
            l, r = i, i+1
            while l >= 0 and r < len_s and s[l] == s[r]:
                if r-l+1 > max_length:
                    st, max_length = l, max(max_length, r-l+1)
                l -= 1
                r += 1
            i += 1
        return s[st: st+max_length]


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("abbd"))
