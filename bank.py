from unicodedata import name

class Account:
    def __init__ (self,name,number):
        self.name=name
        self.number=number
        self.balance= 0
        self.deposits=[]
        self.withdrawals=[]


    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
         self.balance+=amount
         self.deposits.append(amount)
        return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance} and your successful deposit amount is {self.deposits}"

    
    def withdraw(self,amount):
        if amount> self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.withdrawals.append(amount)
            self.transaction_cost=100
            self.balance-=amount + self.transaction_cost
            return f"Hello {self.name} you have withdrawn {amount} your new balance is {self.balance} and successful withdrawal amount is{self.withdrawals}"

    def deposits_statement(self):
        for depos in self.deposits:
            print(f"Your have deposited {depos}")

    def withdrawals_statement (self):
        for withdrawn in self.withdrawals:
            print(f"You have withdrawn: {withdrawn}")
    def balance(self):
        return f"Your balance is {self.balance}"
