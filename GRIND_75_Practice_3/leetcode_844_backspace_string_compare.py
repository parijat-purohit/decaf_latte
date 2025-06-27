class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def format(s, stack):
            for st in s:
                if st == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(st)
            return stack

        st_s = []
        st_t = []
        return format(s, st_s) == format(t, st_t)


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
