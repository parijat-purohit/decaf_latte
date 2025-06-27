class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        map_s = [0]*26
        map_p = [0]*26

        for ch in p:
            map_p[ord(ch) - ord('a')] += 1

        output = []

        for i in range(len(s)):
            map_s[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                map_s[ord(s[i - len(p)]) - ord('a')] -= 1
            if map_s == map_p:
                output.append(i-len(p)+1)

        return output


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
