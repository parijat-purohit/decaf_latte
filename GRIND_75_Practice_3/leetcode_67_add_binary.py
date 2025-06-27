class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) == 1 and a[0] == '0':
            return b
        if len(b) == 1 and b[0] == '0':
            return a

        if len(a) > len(b):
            while len(b) < len(a):
                b = '0' + b
        elif len(b) > len(a):
            while len(a) < len(b):
                a = '0' + a

        sum, carry = "", 0
        for i in range(len(a) - 1, -1, -1):
            x = (int(a[i]) + int(b[i]) + carry) % 2
            sum += str(x)
            carry = (int(a[i]) + int(b[i]) + carry) // 2
        if carry:
            sum += str(carry)
        return sum[::-1]


s = Solution()
# print(s.addBinary("1010", "1011"))
print(s.addBinary("1", "111"))
