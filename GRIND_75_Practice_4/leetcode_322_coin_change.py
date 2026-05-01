class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)

        return dp[amount] if dp[amount] != amount+1 else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
