from collections import defaultdict


class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        def b_search(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l+r)//2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        ind_dict = defaultdict(list)

        for ind, num in enumerate(nums):
            ind_dict[num].append(ind)

        res = [-1]*len(queries)
        n = len(nums)

        for i, q in enumerate(queries):
            if nums[q] in ind_dict:
                if len(ind_dict[nums[q]]) != 1:
                    min_count = float('inf')
                    ind_arr = ind_dict[nums[q]]
                    index_q = b_search(ind_arr, q)
                    if index_q > 0:
                        min_count = min(min_count, abs(q - ind_arr[index_q - 1]),
                                        n - abs(q - ind_arr[index_q - 1]))
                    if index_q < len(ind_arr) - 1:
                        min_count = min(min_count, abs(q - ind_arr[index_q + 1]),
                                        n - abs(q - ind_arr[index_q + 1]))
                    if index_q == 0:
                        min_count = min(min_count, abs(
                            q - ind_arr[-1]), n - abs(q - ind_arr[-1]))
                    if index_q == len(ind_arr) - 1:
                        min_count = min(min_count, abs(
                            q - ind_arr[0]), n - abs(q - ind_arr[0]))
                    res[i] = min_count
        return res


s = Solution()
# print(s.solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
print(s.solveQueries([14, 14, 4, 2, 19, 19, 14, 19, 14], [2, 4, 8, 6, 3]))
