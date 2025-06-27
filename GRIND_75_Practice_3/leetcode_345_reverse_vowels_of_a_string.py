class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        l, r = 0, len(s) - 1
        s = list(s)

        while l < r:
            if s[l] in vowel_set and s[r] in vowel_set:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowel_set:
                r -= 1
            elif s[r] in vowel_set:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)


s = Solution()
print(s.reverseVowels("IceCreAm"))
