class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        ch_map = [0]*26

        for ch in magazine:
            ch_map[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            if ch_map[ord(ch) - ord('a')] == 0:
                return False
            ch_map[ord(ch) - ord('a')] -= 1

        return True


s = Solution()
print(s.canConstruct("aa", "aab"))
print(s.canConstruct('aa', 'ab'))
