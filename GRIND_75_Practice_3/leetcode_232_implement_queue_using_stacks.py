class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.revstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.revstack:
            self.refill()
        return self.revstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.revstack:
            self.refill()
        return self.revstack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.revstack and not self.stack:
            return True
        return False

    def refill(self):
        if not self.revstack:
            for i in range(len(self.stack) - 1, -1, -1):
                self.revstack.append(self.stack[i])
            self.stack = []


q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
