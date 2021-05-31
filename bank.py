from datetime import  datetime
class Account:
    def __init__(self,number,name):
        self.name=name
        self.number=number
        self.balance=0
        self.statement=[]
        
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
        
    

    def borrow(self,amount):
      return f"dear customer {self.name} you have borrowed {amount} ksh"

    def repay_loan(self,amount):
        return f"Hello {self.name} you have repaid {amount}"
    def show_statement(self):
       for transaction in self.statement:
            amount=transaction['amount']
            narration=transaction['narration']
            time=transaction['time']
            date=time.strftime('%d/%m/%y')
            print(f"{date}: {narration} {amount}")


            
     


    
    