class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alpha_map = [0]*26

        for st in s:
            alpha_map[ord(st) - ord('a')] += 1

        for st in t:
            alpha_map[ord(st) - ord('a')] -= 1
            if alpha_map[ord(st) - ord('a')] < 0:
                return False

        for i in range(25):
            if alpha_map[i] != 0:
                return False

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
