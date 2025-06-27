class Solution(object):
    def accountsMerge(self, accounts):
        from collections import defaultdict
        emails_accounts_map = defaultdict(list)
        res = []

        # Build up the graph.
        for account in accounts:
            for email in account[1:]:
                emails_accounts_map[account[1]].append(email)
                emails_accounts_map[email].append(account[1])
        print(emails_accounts_map)
        print('\n')


s = Solution()
print(s.accountsMerge(
    [["John", "a", "b"]]))
