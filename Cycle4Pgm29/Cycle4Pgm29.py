#Create a Bank account with members account number, name, type of account and
#balance. Write constructor and methods to deposit at the bank and withdraw an
#amount from the bank.

class BankAccount:
 
    def __init__(self,acct,name,Atype):
        self.AcctNumber = acct
        self.name = name
        self.Type = Atype
        self.balance = 0

        print("\nAccount number :",self.AcctNumber)
        print("Name :",self.name)
        print("Type of account : ",self.Type)
        
        print("\nYour account is created")

    def deposit(self):
        amount = int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("\nYour new balance = %d"%self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))

        if(amount>self.balance):
            print("\nInsufficient balance!")
        else:
            self.balance= self.balance - amount
            print("\nYour remaining balance = %d" %self.balance)


acct = int(input("Enter your account number:"))
name = input("Enter your account name:")
Atype = input("Enter your account type:")

account=BankAccount(acct,name,Atype)
account.deposit()
account.withdraw()
            
