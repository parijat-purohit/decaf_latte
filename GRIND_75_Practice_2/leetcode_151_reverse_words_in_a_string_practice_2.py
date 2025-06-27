class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        output_s = []
        for st in reversed(s):
            if st != '':
                output_s.append(st)

        return " ".join(output_s)


s = Solution()
print(s.reverseWords("  hello world "))
