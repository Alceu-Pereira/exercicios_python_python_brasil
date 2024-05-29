class bankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def changeName(self, new_name):
        self.name = new_name

    def deposit(self, value):
        self.balance += value

    def withdraw (self, value):
        test_balance = self.balance
        if test_balance - value < 0:
            print('Impossível prosseguir com o saque.')
        else:
            self.balance -= value
            print(f'O saque de R$ {value:.2f} foi realizado com sucesso.')


my_bank_account = bankAccount('Alceu', '12345-65')

my_bank_account.deposit(150)

print(my_bank_account.balance)

my_bank_account.withdraw(50)

print(my_bank_account.balance)

my_bank_account.withdraw(101)

print(my_bank_account.balance)
