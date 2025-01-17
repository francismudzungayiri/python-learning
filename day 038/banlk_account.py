# BANK ACCOUNT SIMULATOR


class BankAccount:
    
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.accounts = {}
        
    #Deposit money    
    def deposit(self, amount):       
        if amount > 0:
            self.balance += amount
            print(f"Desposited ${amount}. New balance: ${self.balance}")
            
        else:
            print('Invalid deposit amount. Amount must be greater than 0.')
            
    
    #withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount<= self.balance:
            self.balance -= amount
            print(f'Withdrew ${amount}, New balance: {self.balance}')
            
        else:
            print('Invalid withdrawal amount or insufficient funds')
            
            
    #check balance
    def check_balance(self):
        print(f'Account balance for {self.account_holder}, balance is ${self.balance}')
        
        
    #show details
    def showdetails(self):
        print('\n ----- Account Details ------ \n')
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Balance: {self.balance}')
    
    #create account
    def createaccount(self):
        name = input('Enter your account holder name : \n').strip()
        initial_deposit = float(input('Enter initial deposit amount \n'))
        account = BankAccount(name, initial_deposit)
        self.accounts[name] = account
        print('ACCOUNT CREATED SUCCESSFULLY')
    
