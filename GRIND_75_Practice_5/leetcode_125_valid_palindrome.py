class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_valid(ch):
            if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                return True
            return False

        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and not is_valid(s[l]):
                l += 1
            while l <= r and not is_valid(s[r]):
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("abc"))
