class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, r = 0, 0
        while r < len(haystack):
            if needle[r-l] == haystack[r]:
                r += 1
            else:
                l += 1
                r = l
            if r - l == len(needle):
                return l
        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("badsadsad", "sad"))
print(s.strStr("mississippi", "issip"))
