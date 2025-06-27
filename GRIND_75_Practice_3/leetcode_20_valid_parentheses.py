class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {'(': ')', '[': ']', '{': '}'}

        for paren in s:
            if paren in paren_map:
                stack.append(paren_map[paren])
            elif not stack or stack.pop() != paren:
                return False
        return not stack


s = Solution()
print(s.isValid("()[]{}"))
