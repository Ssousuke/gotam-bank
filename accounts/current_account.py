from accounts.popular_account import PopularAccount


class CurrentAccount(PopularAccount):
    assure = 15.0

    def super_villain_insurance(self, assure: bool):
        if assure:
            self.balance -= self.assure
