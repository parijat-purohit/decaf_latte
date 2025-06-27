class Balance():
    def __init__(self):
        self.user_hashmap = {}

    def process(self, transactions):
        for t in transactions:
            if t.user in self.user_hashmap:
                self.user_hashmap[t.user] += t.amount
            else:
                self.user_hashmap[t.user] = t.amount
        return self.user_hashmap

    def user_balance(self, user):
        return self.user_hashmap[user]


class Transaction():

    def __init__(self, user, amount):
        self.user = user
        self.amount = amount


t1 = Transaction("Antonio", 300)
t2 = Transaction("Alex", 400)
t3 = Transaction("Antonio", 500)
t4 = Transaction("Alex", 50)

balance = Balance()
print(balance.process([t1, t2, t3]))
print(balance.user_balance("Antonio"))
print(balance.user_balance("Alex"))
print(balance.user_balance("Antonio"))
print(balance.process([t4]))
