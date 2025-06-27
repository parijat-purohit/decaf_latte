class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isvalid(c):
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or "0" <= c <= "9":
                return True

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not isvalid(s[l]):
                l += 1
            while l < r and not isvalid(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("0P"))
