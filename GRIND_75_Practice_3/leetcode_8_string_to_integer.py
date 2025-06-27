class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign_map = {
            '+': 1,
            '-': -1
        }

        result = 0
        sign = None
        min_value = -2**31
        max_value = 2**31 - 1

        for ch in s:
            if not sign and ch == ' ':
                continue
            elif not sign and ch in sign_map:
                sign = sign_map[ch]
            elif 0 <= ord(ch) - ord('0') <= 9:
                if not sign:
                    sign = 1
                result = result*10 + (ord(ch) - ord('0'))
            else:
                break
            if sign and sign*result <= min_value:
                return min_value

            if sign and sign*result >= max_value:
                return max_value

        return sign*result if sign else 0


s = Solution()
# print(s.myAtoi("  -042"))
# print(s.myAtoi("1337c0d3"))
print(s.myAtoi("-91283472332"))
