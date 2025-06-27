class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check_palindrome_length(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = check_palindrome_length(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1
            l2, r2 = check_palindrome_length(i, i+1)
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end+1]


s = Solution()
print(s.longestPalindrome("babad"))
