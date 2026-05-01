"""
Leetcode 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False

        def isValid(ch):
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
                return True
            return False

        l, r = 0, len(s) - 1
        while l <= r:
            if l <= r and not isValid(s[l]):
                l += 1
            elif l <= r and not isValid(s[r]):
                r -= 1
            elif l <= r and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("ap rase"))
print(s.isPalindrome(""))
print(s.isPalindrome("0P"))
