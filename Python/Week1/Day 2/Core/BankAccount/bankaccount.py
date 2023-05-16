class BankAccount:
    balance = 0
    int_rate = 0.01
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
        
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
        
        
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.int_rate*self.balance) + self.balance
        return self
    

        
        
        
        
            
Trump = BankAccount (0.05, 1000)

Tate = BankAccount (0.1, 500)

# Trump_Bankaccount.deposit(200).deposit(200).deposit(100).yield_interest().display_account_info()
Tate.deposit(100).deposit(100).withdraw(1).withdraw(300).withdraw(50).withdraw(50).yield_interest().display_account_info()
