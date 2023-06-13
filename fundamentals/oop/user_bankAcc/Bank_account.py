class BankAccount:
    accounts = 0

    def __init__(self, int_rate, balance):
        self.intrest_rate = int_rate
        self.balance = balance
        BankAccount.accounts += 1

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('Insufficient Funds')
            self.balance -= 5
        return self

    def display_account_info(self):
        # print('========accountinfo===========')
        print('Balance: $' + str(self.balance))
        # print('==============================')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.intrest_rate
        return self

    @classmethod
    def account_numbers(cls):
        print(f'{cls.accounts} accounts in Bank')


user1 = BankAccount(0.1, 500000)
user2 = BankAccount(0.25, 100500)
user1.deposit(500).deposit(4128).deposit(21345).withdraw(100000).yield_interest().display_account_info()
user2.deposit(3124).deposit(23458).withdraw(23487).withdraw(3213).withdraw(2314787).withdraw(321).yield_interest().display_account_info()
# user1.display_account_info()
BankAccount.account_numbers()
