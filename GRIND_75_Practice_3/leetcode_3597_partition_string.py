class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = {}
        l, r = 0, 1

        for _, _ in enumerate(s):
            if s[l:r] in seen:
                r += 1
            else:
                seen[s[l:r]] = True
                l = r
                r = r+1
        return list(seen)


s = Solution()
print(s.partitionString("abbccccd"))
print(s.partitionString("aaaa"))
