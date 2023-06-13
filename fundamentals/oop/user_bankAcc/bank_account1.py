
class BankAccount:

    def __init__ (self, balance, interest):
        self.balance = balance
        self.interest = interest / 100
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}')
        return self


    def withdraw(self, amount):
        self.balance -= amount
        print (f'Withdrew {amount}')
        return self


    def display_account_info(self):
        print('=====Account_Info======')
        print(self.balance)
        print(self.interest)
        print('========================')
        return self


    def yield_interest(self):
        sum = self.balance * self.interest
        self.balance += sum
        print(f'{sum} added to account')
        return self


    # @classmethod
    # def all_accounts(cls):
    #     print(BankAccount.display_account_info())



user1 = BankAccount(10000, 20)
user2 = BankAccount(30000, 15)

user1.deposit(1500).deposit(2500).deposit(9329).withdraw(10000).yield_interest().display_account_info()

user2.deposit(2100).deposit(3140).withdraw(2200).withdraw(1100).withdraw(3000).withdraw(9999).yield_interest().display_account_info()

# print(BankAccount.all_accounts())

