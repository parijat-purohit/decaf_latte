from collections import defaultdict


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_to_s = {}
        s_to_pattern = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i, p in enumerate(pattern):
            if p in pattern_to_s:
                if s[i] != pattern_to_s[p]:
                    return False
            else:
                pattern_to_s[p] = s[i]

        for i, st in enumerate(s):
            if st in s_to_pattern:
                if s_to_pattern[st] != pattern[i]:
                    return False
            else:
                s_to_pattern[st] = pattern[i]
        return True


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("abc", "b c a"))
