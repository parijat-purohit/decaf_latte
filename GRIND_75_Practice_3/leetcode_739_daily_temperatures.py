class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0]*len(temperatures)

        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, i = stack.pop()
                output[i] = day - i
            stack.append((temp, day))
        return output


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
