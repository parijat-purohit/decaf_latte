# Solution 1

# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         count = 0
#         for i in range(len(s)):
#             count += map[s[i]]
#             if i < len(s) - 1:
#                 if s[i] == 'I' and s[i+1] in ['V', 'X']:
#                     count -= 2*map[s[i]]
#                 elif s[i] == 'X' and s[i+1] in ['L', 'C']:
#                     count -= 2*map[s[i]]
#                 elif s[i] == 'C' and s[i+1] in ['D', 'M']:
#                     count -= 2*map[s[i]]
#         return count

# Solution 2
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, count = 0, 0
        for st in reversed(s):
            curr = map[st]
            if curr >= prev:
                count += curr
            else:
                count -= curr
            prev = curr
        return count


s = Solution()
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
