class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_value = 2**31 - 1
        min_value = -2**31

        s = s.strip()

        sign = 1
        sign_map = {
            '+': +1,
            '-': -1
        }
        total = 0

        for i in range(len(s)):
            if i == 0 and s[i] in sign_map:
                sign = sign_map[s[i]]
            else:
                if '0' <= s[i] <= '9':
                    total = total*10 + int(s[i])
                else:
                    break
            if sign * total >= max_value:
                return max_value
            if sign * total <= min_value:
                return min_value
        return sign*total


s = Solution()
print(s.myAtoi("      1337c0d3"))
print(s.myAtoi("+1"))
print(s.myAtoi("42"))
