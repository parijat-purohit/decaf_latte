"""
Leetcode 409: Longest Palindrome
Time Complexity: O(len(string))
Space Complexity: O(1)

If we treat the input set bounded by an upper limit say 52 chars or all the unicode literals,
We can say that it's O(1) as the size would not grow if input size grows towards infinity.
However, if the set can't be bounded, then we have to consider it as O(N).
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_map = [0]*52

        for st in s:
            if 'A' <= st <= 'Z':
                c_map[ord(st) - ord('A')] += 1
            else:
                c_map[ord(st) - ord('a') + 26] += 1

        max_len = 0
        odd_taken = False

        for c in c_map:
            max_len += (c//2)*2
            if c % 2 != 0 and not odd_taken:
                max_len += 1
                odd_taken = True
        return max_len


s = Solution()
print(s.longestPalindrome("aaaaAaaa"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("abcccccdd"))
