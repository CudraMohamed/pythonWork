from datetime import datetime

class Account:
    def __init__ (self,name,number):
        self.name=name
        self.number=number
        self.balance= 0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction_cost=100
        self.now='{:%A-%B-%d %H:%M:%S}'.format(datetime.now())
        self.withdrawal_dict={}
        self.deposit_dict={}

    def deposit(self,amount):
        
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
         self.balance+=amount
         self.deposits.append(amount)
         self.deposit_dict['date']=self.now
         self.deposit_dict['amount']=amount
         self.narration= f"Hello {self.name}. Confirmed on {self.now} you deposited {amount} and your new balance is {self.balance}. Your successful deposit amount is {self.deposits}  "
         self.deposit_dict['narration']=self.narration
         return self.deposit_dict

    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.withdrawals.append(amount)
            self.balance-=amount + self.transaction_cost
            self.withdrawal_dict['date']=self.now
            self.withdrawal_dict['amount']=amount
        if amount+self.transaction_cost > self.balance:
             self.narration= f"Hello {self.name}.Confirmed on {self.now} you have withdrew {amount} and your new balance is {self.balance}. Your successful withdrawal amount is{self.withdrawals}"
             self.withdrawal_dict['narration']=self.narration
             return self.withdrawal_dict
            # withdrawable_balance=self.balance-self.transaction_cost
            # if amount>withdrawable_balance:
            #     return "insufficient funds"

    def deposits_statement(self):
       
        for depos in self.deposits:
            print(f"Your have deposited {depos} on {self.now}")

    def withdrawals_statement (self):
        
        for withdrawn in self.withdrawals:
            print(f"You have withdrawn: {withdrawn} on {self.now}")
    def current_balance(self):
       
        return f"Hello {self.name} your current balance is {self.balance} {self.now}"
