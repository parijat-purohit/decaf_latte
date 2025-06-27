import heapq


class MedianFinder(object):

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.max_heap or (self.max_heap and num <= -self.max_heap[0]):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        self.heap_balance()

    def heap_balance(self):
        if len(self.max_heap) - len(self.min_heap) >= 2:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)
        elif len(self.min_heap) > len(self.max_heap):
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) != len(self.min_heap):
            return -self.max_heap[0]
        else:
            return float(-self.max_heap[0] + self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
