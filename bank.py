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
        self.both_statements=[]
        self.loan_balance=0
        

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

    def deposits_statement(self):
       
        for depos in self.deposits:
            print(f"Your have deposited {depos} on {self.now}")

    def withdrawals_statement (self):
        
        for withdrawn in self.withdrawals:
            print(f"You have withdrawn: {withdrawn} on {self.now}")
    def current_balance(self):
       
        return f"Hello {self.name} your current balance is {self.balance} {self.now}"

    def full_statement(self):
        for item in self.both_statements:
            self.both_statements.sort(key=lambda item: item['date'], reverse=True)
            date=item['amount']
            amount=item['amount']
            narration=item['narration']
            print(f"{date}{narration}{amount}")
        # self.both=[self.withdrawals,self.deposits]
        # self.both_statements.extend(self.both)
        # for transaction in self.both_statements:
        #     time= datetime("%H:%M:%S")
        #     print(f"{time} Deposit {transaction}",sep="\n")

    def borrow(self,loan):
        counting=sum(self.deposits)
        qualification_amount=counting*(1/3)
        loan+=loan*(30/100)
        if len(self.deposits) < 10 :
            return f"Sorry {self.name} you must have more than 10 deposits to get a loan"
        elif self.loan_amount <= 100:
            return f"Sorry {self.name} . Please enter an amount more than 100"
        elif loan >= qualification_amount:
            return f"You cannot borrow more than {counting//3}"
        elif self.loan_balance > 0:
            return f"Dear customer, your outstanding loan balance is {self.loan_balance}"
        else:
            self.loan_balance +=loan
            return f"Your loan balance is {self.loan_balance}"

    def loan_repayment(self,amount):
        if amount < self.loan_balance:
            self.loan_balance-=amount
            return f"You have paid {amount} and you have an outstanding balance is {self.loan_balance}"

        else:
            self.loan_balance-=amount
            overpayment=amount-self.loan_balance
            self.balance+=overpayment
            return f"You loan is fully paid"

        # def transfer(self,amount,account):
        #     if amount > self.balance:
        #         return f"Cannot tranfer amount.Your account balance is too low"
        #     elif amount <=0:
        #         return f"Enter an amount more than 0"
        #     else:
        #         self.balance-=amountaccount.balance += amount
        #         return f"You have sent {amount} to {account.account_name} and your balance is {self.balance}"

            


# acc=Account(name="cudra",number="2345678")
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(1000))
# print(acc.deposit(100))
# print(acc.withdraw(11000))
# print(acc.borrow(1000))
            # return self.loan_balance

    
