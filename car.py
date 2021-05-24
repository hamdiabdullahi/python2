class Bank:
    accountNumber=3456
    def __init(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self):
         return f"I am withdrawing from account{self.name}"
    def deposit(self):
        return f"I deposited and the balance is{self.balance}"
