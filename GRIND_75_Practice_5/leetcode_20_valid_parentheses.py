"""
Leetcode 20. Valid Parentheses
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for st in s:
            if st in parentheses_map:
                stack.append(parentheses_map[st])
            elif not stack or stack.pop() != st:
                return False
        return not stack


s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("({]}"))
