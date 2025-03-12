class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        tokens = s.split(" ")
        x = ""

        for token in tokens:
            if token != '':
                x = token + " " + x

        return x[:-1]


s = Solution()
print(s.reverseWords("the sky is blue  "))
