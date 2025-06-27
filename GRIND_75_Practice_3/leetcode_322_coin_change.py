# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         memo = {}

#         def dfs(amount):
#             if amount == 0:
#                 return 0
#             if amount in memo:
#                 return memo[amount]
#             res = 2**31 - 1
#             for c in coins:
#                 if amount - c >= 0:
#                     res = min(res, 1 + dfs(amount-c))
#                 memo[amount] = res
#             return memo[amount]

#         min_count = dfs(amount)
#         return min_count if min_count != 2**31 - 1 else -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for amount in range(1, amount+1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount-coin])
                """
                We can't use else block if the coins are not sorted.
                It's not a guarantee that the coins will be sorted.
                If so, we can break the loop and optimize the runtime by
                not checking other coins.
                """
                # else:
                #     break
        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2, 4, 6], 10))
