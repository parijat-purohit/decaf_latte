"""
Leetcode 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n)
Space Complexity: O(n) Additional stack can store all the brackets in s.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesis_map = {'(': ')', '{': '}', '[': ']'}
        st = []

        for bracket in s:
            if bracket in parenthesis_map:
                st.append(parenthesis_map[bracket])
            elif not st or st.pop() != bracket:
                return False
        return not st


s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([)]"))
