
from Bank_account import BankAccount


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)


    def display_info(self):
        print('==================================')
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email:{self.email}')
        print(f'Age: {self.age}')
        print(f'Rewards member: {self.is_rewards_member}')
        print(f'Gold points: {self.gold_card_points}')
        print('==================================')
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        else:
            print('User already a member.')
            return False

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print('insufficent funds')
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_witdrawl(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print('Account Balance:', self.account.balance)

John = User('John', 'Tran', 'namesjohntran@gmail.com', 31)
Greg = User('Greg', 'Blake', 'Blakey@gmail.com', 56)
Marvin = User('Marvin', 'Pascua', 'Marvstar@gmail.com', 29)

print(John.email)

John.enroll()
Greg.enroll()
print(John.gold_card_points)
Greg.enroll()

John.spend_points(50)
Greg.spend_points(80)
print('Greg has', Greg.gold_card_points,'left.')

print("John has", John.gold_card_points,'left.')
John.display_info()
Greg.display_info()
Marvin.display_info()

John.display_info().spend_points(25).display_info().enroll()
John.display_info()


John.make_deposit(2000)
John.make_witdrawl(3000)
John.display_user_balance()