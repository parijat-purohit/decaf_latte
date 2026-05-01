class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum, digit_product, m = 0, 1, n

        while (m > 0):
            digit_sum += m % 10
            digit_product *= m % 10
            m //= 10
        return True if n % (digit_sum + digit_product) == 0 else False


s = Solution()
print(s.checkDivisibility(99))
print(s.checkDivisibility(23))
