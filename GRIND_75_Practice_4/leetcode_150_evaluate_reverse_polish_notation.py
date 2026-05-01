class Solution:
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        operation = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y)

        }
        st = []
        for token in tokens:
            if token in operators:
                b = st.pop()
                a = st.pop()
                st.append(operation[token](a, b))
            else:
                st.append(int(token))
        return st[-1]


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
