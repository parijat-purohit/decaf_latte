import heapq


def findMedian(arr):
    heapq.heapify(arr)
    fixed_n, n = len(arr), len(arr)
    n = n//2 if n % 2 == 1 else n//2 - 1
    print('val', n)
    while (n):
        heapq.heappop(arr)
        n -= 1
    if fixed_n % 2 != 0:
        return heapq.heappop(arr)
    else:
        m1 = heapq.heappop(arr)
        m2 = heapq.heappop(arr)
        return (m1 + m2)/2.0


print(findMedian([2, 1, 3, 5, 4]))
print(findMedian([2, 1, 3, 6, 4, 5]))
