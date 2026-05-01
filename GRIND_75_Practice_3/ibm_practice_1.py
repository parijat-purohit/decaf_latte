class Solution(object):
    def stringmanipulate(self, arr):
        res = ""
        for c in arr:
            if c == 'a':
                res += 'z'
            else:
                res += chr(ord(c) - 1)
        return res


s = Solution()
print(s.stringmanipulate("hackerrank"))
