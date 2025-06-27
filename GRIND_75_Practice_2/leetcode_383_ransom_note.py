class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = [0]*26

        for c in magazine:
            counter[ord(c) - ord('a')] += 1

        for c in ransomNote:
            if counter[ord(c) - ord('a')] == 0:
                return False
            counter[ord(c) - ord('a')] -= 1
        return True


s = Solution()
print(s.canConstruct("aa", "aab"))
