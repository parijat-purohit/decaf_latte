class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_value_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.min_value_stack or val <= self.min_value_stack[-1]:
            self.min_value_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min_value_stack[-1]:
            self.min_value_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return self.min_value_stack[-1]


ms = MinStack()
ms.push(3)
ms.push(2)
print(ms.stack)
ms.pop()
print("min_stack", ms.min_value_stack[-1])
print(ms.getMin())
ms.push(1)
print(ms.top())
print(ms.getMin())
