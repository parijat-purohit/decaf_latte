class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.rev_stack = []

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
        self.check()
        return self.rev_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.check()
        return self.rev_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stack or self.rev_stack)

    def check(self):
        if self.stack and not self.rev_stack:
            while self.stack:
                self.rev_stack.append(self.stack.pop())


my_queue = MyQueue()
my_queue.push(5)
my_queue.push(3)
print(my_queue.peek())
print(my_queue.pop())
print(my_queue.pop())
print(my_queue.empty())
