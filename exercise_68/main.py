class InvestimentAccount:
    def __init__(self, start_balance=1000, interest_rate=0.1):
        self.start_balance = start_balance
        self.interest_rate = interest_rate

    
    def increase_interest(self):
        self.start_balance += (self.start_balance * self.interest_rate)


contaDeInvestimento = InvestimentAccount()

print(contaDeInvestimento.start_balance)
contaDeInvestimento.increase_interest()
contaDeInvestimento.increase_interest()
contaDeInvestimento.increase_interest()
contaDeInvestimento.increase_interest()
contaDeInvestimento.increase_interest()
print(contaDeInvestimento.start_balance)
