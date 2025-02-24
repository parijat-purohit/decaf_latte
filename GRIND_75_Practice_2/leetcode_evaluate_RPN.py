class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        if len(tokens) == 1:
            return int(tokens[0])

        st = []

        for token in tokens:
            if token in op_map:
                b = st.pop()
                a = st.pop()
                st.append(op_map[token](a, b))
            else:
                st.append(int(token))
        return st[0]


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
