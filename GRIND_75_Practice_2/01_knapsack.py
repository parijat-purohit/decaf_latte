class Solution(object):
    def knapsack(self, profit, weight, W):
        memo = {}

        def dfs(i, w):
            if i == len(weight):
                return 0

            if (i, w) in memo:
                return memo[(i, w)]

            include_profit = 0
            if w - weight[i] >= 0:
                include_profit = profit[i] + dfs(i+1, w-weight[i])
            exclude_profit = dfs(i+1, w)
            memo[(i, w)] = max(include_profit, exclude_profit)
            return memo[(i, w)]

        max_profit = dfs(0, W)

        return max_profit


# class Solution(object):
#     def knapsack(self, profit, weight, W):
#         memo = {}

#         def dfs(i, w):
#             if i == len(weight):
#                 return 0

#             if (i, w) in memo:
#                 return memo[(i, w)]
#             if w + weight[i] > W:
#                 memo[(i, w)] = dfs(i+1, w)
#             else:
#                 memo[(i, w)] = max(dfs(i+1, w),
#                                    profit[i] + dfs(i+1, w+weight[i]))
#             return memo[(i, w)]

#         max_profit = dfs(0, 0)

#         return max_profit


s = Solution()
print(s.knapsack([5, 4, 8], [1, 5, 3], 5))
