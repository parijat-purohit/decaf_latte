class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        final_num, mul = 0, 1

        while n > 0:
            if n % 10 != 0:
                final_num = (n % 10)*mul + final_num
                mul *= 10
            print(n)
            n //= 10
        return final_num


s = Solution()
print(s.removeZeros(1020030))
