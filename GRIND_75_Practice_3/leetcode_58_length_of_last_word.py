class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st_len = len(s)
        right, left = None, None
        for i in range(st_len-1, -1, -1):
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                if not left and not right:
                    left, right = i, i
                else:
                    left = i

            elif left and right and s[i] == ' ':
                break

        return right - left + 1


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))
print(s.lengthOfLastWord("a"))
print(s.lengthOfLastWord("a "))
