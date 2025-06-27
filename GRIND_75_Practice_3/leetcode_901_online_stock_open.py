class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.st and self.st[-1][1] <= price:
            span += self.st.pop()[0]
        self.st.append([span, price])
        return span


s = StockSpanner()
print(s.next(28))
print(s.next(14))
print(s.next(28))
print(s.next(35))
print(s.next(46))
print(s.next(53))
print(s.next(66))
print(s.next(80))
print(s.next(87))
print(s.next(88))
