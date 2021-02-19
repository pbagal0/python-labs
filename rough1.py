

#Bank Account

class Bank:

    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,a):
        if self.balance < a:
            raise balanceinsufficent
        self.balance=self.balance-a

    def credit(self,a):
        self.balance=self.balance+a

class balanceinsufficent(Exception):
    def __str__(self):
        return f"Insu"
a1 = Bank("prashant",9900,10000)
try:
    a1.debit(11000)
except balanceinsufficent as e:
    print(balanceinsufficent)