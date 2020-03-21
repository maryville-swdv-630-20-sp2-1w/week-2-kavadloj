class CheckingAccount:

    def __init__(self, name, address, accountNumber, balance):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber
        self.__balance = balance

    def credit(self, amount):
        print("${:.2f} has been credited to the account {}".format(amount, self.name))
        self.__balance = self.__balance + amount
   
    def debit(self, amount):
        if self.__balance < amount:
            print("Debit was not performed because debiting ${:.2f} from the account would result in an overdraft".format(amount))
        else:
            print("${:.2f} has been debited from the account {}".format(amount, self.name))
            self.__balance = self.__balance - amount

    def getBalance(self):
        print("Account name: {}, Balance: ${:.2f}".format(self.name, self.__balance))