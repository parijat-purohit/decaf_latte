class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0

        for account in accounts:
            sum_wealth = sum(account)
            max_wealth = max(max_wealth, sum_wealth)

        return max_wealth


s = Solution()
print(s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
