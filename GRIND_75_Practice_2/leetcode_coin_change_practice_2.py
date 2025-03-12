class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        max_amount = amount + 1

        def dfs(index, amount):
            if amount == 0:
                return 0
            if index == len(coins):
                return max_amount
            if (index, amount) in memo:
                return memo[(index, amount)]

            included_res = 0
            if amount - coins[index] >= 0:
                included_res = 1 + dfs(index+1, amount - coins[index])
            excluded_res = dfs(index+1, amount)
            memo[(index, amount)] = min(included_res, excluded_res)
            return memo[(index, amount)]

        min_coins = dfs(0, amount)
        return min_coins if min_coins != max_amount else -1


s = Solution()
print(s.coinChange([1, 2, 3, 4, 5], 5))
