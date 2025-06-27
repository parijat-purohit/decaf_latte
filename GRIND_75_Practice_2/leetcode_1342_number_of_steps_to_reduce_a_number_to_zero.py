class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0

        while num > 0:
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                num -= 1
                count += 1
        return count


s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(123))
