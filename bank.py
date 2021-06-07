from datetime import  datetime
class Account:
    def __init__(self,number,name):
        self.name=name
        self.number=number
        self.balance=0
        self.statement=[]
        self.loan=0
        
    def show_balance(self):
      return f"hello {self.name} your balance is{self.balance}"

    def deposit(self,amount):
      if amount<0:
        
         
         return f"hello {self.name} your balance is {self.balance}"

             
      else:
        self.balance+=amount
        now=datetime.now()
        transaction={
            'amount':amount,
             'time':now,
             'narration':'you deposited'
         }
        self.statement.append(transaction)
      return self.show_balance()
      
    def withdraw(self,amount):
      if self.balance<amount:
        return f"dear customer {self.name} your balance is {self.balance} you cannot withdraw {amount}"
      else:   
        self.balance-=amount
        now=datetime.now()
        transaction={
            'amount':amount,
             'time':now,
             'narration':'you withdrew'
         }
        self.statement.append(transaction)
      return self.show_balance()
        
    

    # def borrow(self,amount):
      # return f"dear customer {self.name} you have borrowed {amount} ksh"

    # def repay_loan(self,amount):
        # return f"Hello {self.name} you have repaid {amount}"
    def show_statement(self):
       for transaction in self.statement:
            amount=transaction['amount']
            narration=transaction['narration']
            time=transaction['time']
            date=time.strftime('%d/%m/%y')
            print(f"{date}: {narration} {amount}")
    def borrow_loan(self,amount,):
      if amount<0:
        return f"You {self.amount} already have no loan {amount}" 
      elif self.loan>0:
         return f"You are having {self.loan} a loan "
      elif amount<0.1*self.balance:
        return f"kindly give me {amount} loan "
      else:

        loan=amount*1.05 
      self.loan=loan
      self.balance += amount
      return f"You have successfully borrowed {self.loan}"
    def repay_loan(self,amount):
      if amount<0:
        return f"You have an extra amount{amount} in the bank"
      elif amount<self.loan:
        self.loan-=amount
        now=datetime.now()
        transaction={
           'amount':amount,
             'time':now,
             'narration':'you repayed'
        }
        self.show_statement.append(transaction)
        return f"Hello {self.loan} decrease loan with {amount}"
      else:
        diff=amount-self.loan
        self.loan=0
        self.deposit(diff)
        now=datetime.now()
        transaction={
           'amount':amount,
             'time':now,
             'narration':'you repayed loan successfully'
        }
        self.show_statement.append(transaction)
        return f"Hello you have fully repaid your loan"

     

            