class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])

        st = []
        op_map = {'+': lambda x, y: x+y,
                  '-': lambda x, y: x-y,
                  '*': lambda x, y: x*y,
                  '/': lambda x, y: int(x/y)
                  }

        for token in tokens:
            if token in op_map:
                op2 = st.pop()
                op1 = st.pop()
                st.append(op_map[token](op1, op2))
            else:
                st.append(int(token))

        return st[0]


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
