class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        n1 = 1
        n2 = 2

        for _ in range(3, n+1):
            n1, n2 = n2, n1 + n2

        return n2


s = Solution()
print(s.climbStairs(4))
