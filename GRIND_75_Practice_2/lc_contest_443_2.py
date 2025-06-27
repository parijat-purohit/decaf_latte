class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def rev(st):
            rev_s = ""
            for s in st:
                rev_s = s + rev_s
            return rev_s

        max_len = 0
        len_s = len(s)
        len_t = len(t)

        for i in range(len_s+1):
            for j in range(i, len_s+1):
                for k in range(len_t+1):
                    for l in range(k, len_t + 1):
                        first_sub = s[i:j]
                        second_sub = t[k:l]
                        print(first_sub, second_sub)
                        comb_str = first_sub + second_sub
                        if comb_str == rev(comb_str):
                            max_len = max(max_len, len(comb_str))
                        if first_sub == rev(first_sub):
                            max_len = max(max_len, len(first_sub))
                        if second_sub == rev(second_sub):
                            max_len = max(max_len, len(second_sub))
        return max_len


s = Solution()
print(s.longestPalindrome("abcde", "ecdba"))
print(s.longestPalindrome("a", "bbbb"))
