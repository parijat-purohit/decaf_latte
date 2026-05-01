class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        output = []
        arr.sort()
        abs_diff = float('inf')
        for i in range(len(arr)-1):
            abs_diff = min(abs_diff, abs(arr[i] - arr[i+1]))

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) == abs_diff:
                output.append((arr[i], arr[i+1]))

        return output


s = Solution()
print(s.minimumAbsDifference([4, 2, 1, 3]))
print(s.minimumAbsDifference([1, 3, 6, 10, 15]))
