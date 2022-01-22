from exceptions.exception import DomainException


class Account(object):
    def __init__(self, number, name, balance, status):
        if status:
            self.number = number
            self.name = name
            self.balance = balance
            self.status = status
        else:
            raise AttributeError(f'your account is inaccessible! contact the gotambank')

    def limit(self):
        return self.balance + (self.balance * 0.20)

    def withdraw(self, amount):
        if amount > self.balance:
            raise DomainException('insufficient funds')
        elif amount < 10.0:
            raise DomainException('the minimum withdraw amount is 10.0 R$')
        else:
            self.balance -= amount

    def deposit(self, amount):
        if amount <= 10.0:
            raise DomainException('the minimum deposit amount is 10.0 R$')
        else:
            self.balance += amount

    def extract(self):
        print(f'Conta: {self.number}')
        print(f'Nome: {self.name}')
        print(f'Saldo: {self.balance}')
        print(f'Limite: {self.limit()}')
        print(f'Status da conta: {self.status}')
