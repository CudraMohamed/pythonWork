from unicodedata import name


class Account:
    def __init__(self,bank_name,acc_number,balance,password):
        self.bank_name=bank_name
        self.acc_number=acc_number
        self.balance=balance
        self.password=password

    def deposit(self):
        dep_amount=int(input('Enter amount you want to deposit : '))
        dep_amount+=self.balance
        return f'Your new balance is {dep_amount}'

    def withdraw(self):
        wthdr_amount = int(input('Enter amount you want to withdraw : '))
        self.balance-=wthdr_amount
        return f'Your new balance is{self.balance}'