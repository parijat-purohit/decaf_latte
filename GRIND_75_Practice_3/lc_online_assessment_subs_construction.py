from collections import Counter


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False

        ctr = Counter(s)
        sub_str = s[:len(ctr)]

        for i in range(0, len(s), len(sub_str)):
            if sub_str != s[i: i+len(sub_str)]:
                return False
        return True


s = Solution()
print(s.repeatedSubstringPattern("abaababaab"))
print(s.repeatedSubstringPattern("aba"))
