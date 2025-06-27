from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(len(accounts))
        email_list = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_list:
                    uf.union(i, email_list[email])
                else:
                    email_list[email] = i

        email_dict = defaultdict(list)

        for email, i in email_list.items():
            leader = uf.find(i)
            email_dict[leader].append(email)

        res = []

        for i in email_dict:
            name = accounts[i][0]
            res.append([name] + sorted(email_dict[i]))

        return res


s = Solution()
print(s.accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co",
      "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
