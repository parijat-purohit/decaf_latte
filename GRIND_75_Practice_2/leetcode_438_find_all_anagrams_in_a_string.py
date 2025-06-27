class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        map_p = [0]*26
        map_s = [0]*26
        for st in p:
            map_p[ord(st) - ord('a')] += 1

        output = []
        len_p = len(p)
        for i in range(len(s)):
            map_s[ord(s[i]) - ord('a')] += 1
            if i >= len_p:
                map_s[ord(s[i - len_p]) - ord('a')] -= 1
            if map_s == map_p:
                output.append(i-len_p+1)
        return output


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("acdcaeccde", 'c'))
