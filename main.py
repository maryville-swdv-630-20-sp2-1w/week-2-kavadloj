from CheckingAccount import *

name = input("Create an account name: ")
address = input("Enter address of account holder: ")
accountNum = input("Enter an account number: ")
balance = int(input("Enter starting balance: "))

myAccount = CheckingAccount(name, address, accountNum, balance)

while True:
    
    option = input("\nPress 1 to debit the account, 2 to credit the account, 3 to check the account balance, or 4 to quit: ")
    
    if option == "1":
        amount = int(input("Enter an amount: "))
        myAccount.debit(amount)
    
    elif option == "2":
        amount = int(input("Enter amount: "))
        myAccount.credit(amount)
    
    elif option == "3":
        myAccount.getBalance()
    
    else:
        break