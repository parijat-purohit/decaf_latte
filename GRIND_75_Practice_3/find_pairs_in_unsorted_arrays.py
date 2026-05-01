class Solution():
    def findPairs(self, a, b):
        a.sort()
        b.sort()
        print(a, b)


s = Solution()
print(s.findPairs([7, 2, 10, 15, 12, 9], [10, 8, 5, 3, 4, 7]))
