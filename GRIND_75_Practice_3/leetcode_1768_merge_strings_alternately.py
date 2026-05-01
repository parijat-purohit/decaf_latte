class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = min(len(word1), len(word2))
        s = ""
        for i in range(n):
            s += word1[i]+word2[i]

        s += word1[n:] if len(word1) > len(word2) else word2[n:]
        return s


s = Solution()
print(s.mergeAlternately("ab", "pqrs"))
  