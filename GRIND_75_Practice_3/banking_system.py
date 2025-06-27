from abc import ABC, abstractclassmethod
import uuid
import time


class Client():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def lookup(self):
        return self.balance

    def details(self):
        return self.__dict__


class Transaction(ABC):
    @abstractclassmethod
    def process(self):
        pass


class Send(Transaction):
    def __init__(self, sender, receiver, amount):
        self.id = uuid.uuid4()
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.processed = False

    def details(self):
        return self.__dict__

    def process(self):
        if self.processed:
            
            sender_balance = self.sender.balance
            if sender_balance > 0 and sender_balance - self.amount >= 0:
                self.sender.balance -= self.amount
                self.receiver.balance += self.amount
                self.processed = True
            else:
                raise ValueError("Insufficient amount for a transaction")
        else:
            self.retry()

    def

c1 = Client("a", 100)
c2 = Client("b", 200)
c3 = Client("c", 500)
print(c1.lookup(), c2.lookup())
s1 = Send(c1, c2, 10)
print(s1.details())
print(c1.lookup(), c2.lookup())
