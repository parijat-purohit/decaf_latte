# an element is pushed and popped exactly once.
# hence, the total time complexity is O(2N).
# It is never O(N^2).
# We use Monotonic Stack to solve the problem.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        st = []
        res = [0]*len(temperatures)

        for pos, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                _, i = st.pop()
                res[i] = pos - i
            st.append((temp, pos))
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 40, 50, 60]))
