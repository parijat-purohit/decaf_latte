class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = [0]*52

        for st in s:
            if 'a' <= st <= 'z':
                map[ord(st)-ord('a')] += 1
            else:
                map[ord(st) - ord('A')+26] += 1

        sum, carry = 0, 0
        for mp in map:
            sum += 2*(mp//2)
            if mp % 2 == 1 and not carry:
                carry = 1

        return sum + carry


s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("ccc"))
