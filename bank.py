
class Account:
    def __init__(self,number,name):
        self.name=name
        self.number=number
        self.balance=0
        
    def show_balance(self):
      return f"hello {self.name} your balance is{self.balance}"

    def deposit(self,Amount):
      if Amount>0:
         return f"hello {self.name} your balance is {self.balance}"
             
      else:
         return f"Dear customer {self.name} your account is negative"
       

    def withdraw(self,amount):
      if self.balance>amount:
         return f"dear customer {self.name} your balance is {self.balance} you cannot withdraw {amount}"
      else:   
        self.balance-=amount
        return f"Hello {self.name} you have deposited {amount} you cannot withdraw {self.show_balance()}"
    

    def borrow(self,amount):
      return f"dear customer {self.name} you have borrowed {amount} ksh"

    def repay_loan(self,amount):
        return f"Hello {self.name} you have repaid {amount}"


    
    