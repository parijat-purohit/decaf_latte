class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        sign_map = {
            '+': 1,
            '-': -1
        }
        num = 0
        max_val = 2**31 - 1
        min_val = -2**31

        s = s.strip(" ")

        for i, st in enumerate(s):
            if i == 0 and st in sign_map:
                sign = sign_map[st]
            elif st >= '0' and st <= '9':
                num = num*10 + int(st)
                if sign*num > max_val:
                    return max_val
                elif sign*num < min_val:
                    return min_val
            else:
                return sign*num
        return sign*num


s = Solution()
print(s.myAtoi("-042"))
