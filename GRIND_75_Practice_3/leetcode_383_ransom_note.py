class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_map = [0]*26
        for ch in magazine:
            char_map[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            char_map[ord(ch) - ord('a')] -= 1
            if char_map[ord(ch) - ord('a')] < 0:
                return False
        return True


s = Solution()
print(s.canConstruct("aa", "aab"))
