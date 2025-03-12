class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount-c))
            memo[amount] = res
            return res

        min_count = dfs(amount)
        return min_count if min_count != 1e9 else -1


s = Solution()
print(s.coinChange([2, 3], 5))

# Let's consider a variation where one coin can be used only once.
# It will turn into a 0/1 Knapsack style solution.


# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         memo = {}

#         def dfs(index, amount):
#             if amount == 0:
#                 return 0
#             if index >= len(coins) or amount < 0:
#                 return 1e9
#             if (index, amount) in memo:
#                 return memo[(index, amount)]

#             memo[(index, amount)] = min(dfs(index+1, amount),
#                                         1 + dfs(index+1, amount - coins[index]))
#             return memo[(index, amount)]

#         result = dfs((0, amount))

#         return result if result != 1e9 else -1
