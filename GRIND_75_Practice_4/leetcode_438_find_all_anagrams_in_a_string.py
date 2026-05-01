class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_map, s_map = [0]*26, [0]*26

        if len(s) < len(p):
            return []

        for i in range(len(p)):
            p_map[ord(p[i]) - ord('a')] += 1
            s_map[ord(s[i]) - ord('a')] += 1

        output = []

        l, r = 0, len(p)-1

        while r < len(s):
            if s_map == p_map:
                output.append(l)
            s_map[ord(s[l]) - ord('a')] -= 1

            l += 1
            r += 1
            if r < len(s):
                s_map[ord(s[r]) - ord('a')] += 1

        return output
