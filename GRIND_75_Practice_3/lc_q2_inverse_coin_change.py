class Solution:
    def findCoins(self, numWays):
        n = len(numWays)
        dp = [0] * (n + 1)
        dp[0] = 1
        coins = []

        for i in range(1, n + 1):
            if numWays[i-1] > dp[i]:
                coins.append(i)
                for j in range(i, n+1):
                    dp[j] += dp[j-i]
                if numWays[i-1] > dp[i]:
                    return []
            elif numWays[i-1] < dp[i]:
                return []
        return coins


s = Solution()
print(s.findCoins([0, 1, 0, 2, 0, 3, 0, 4, 0, 5]))
print(s.findCoins([1, 2, 3, 4, 15]))
