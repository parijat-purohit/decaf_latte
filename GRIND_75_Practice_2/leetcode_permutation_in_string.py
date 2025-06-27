class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_count = [0]*26
        s2_count = [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            match += (1 if s1_count[i] == s2_count[i] else 0)

        print(match)


s = Solution()
s.checkInclusion("ab", "eidbaooo")
