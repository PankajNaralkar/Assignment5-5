class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        pass
    
    def withdrawal(self, amount):
        self.balance=self.balance-amount
        pass
    def deposit(self, amount):
        self.balance=self.balance+amount
        pass
    def getBalance(self):
        return self.balance
    pass

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
            pass
    
    def interestAmount(self):
        return (self.interestRate * self.balance / 100)
    pass

demo1= SavingsAccount("Ashish", 2000, 5)
demo2= Account("Ashish", 2000)
    
x=SavingsAccount()
x.interestAmount()
print("------------------------")
x=Account()
x.balance()
x.withdrawal()
x.getBalance()
print("--------------")
x=Account()
x.balance()
x.deposit()
x.getBalance()
