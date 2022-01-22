from accounts.account import Account


class PopularAccount(Account):
    def limit(self):
        return self.balance + (self.balance * 0.40)

    def transfer(self: Account, account_receive: Account, amount):
        if account_receive:
            self.withdraw(amount)
            account_receive.deposit(amount)
