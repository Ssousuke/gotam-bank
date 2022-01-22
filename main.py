from accounts.account import Account
from accounts.popular_account import PopularAccount
from exceptions.exception import DomainException
try:
    # Instancia duas contas
    account1 = Account(10001, 'Bruce Wayne', 0.0, True)
    account2 = PopularAccount(10002, 'Marta Wayne', 0.0, True)

    # Depositar
    account1.deposit(100.0)
    account2.deposit(100.0)

    # Saque
    account1.withdraw(10.0)
    account2.withdraw(10.0)

    # Transferencia
    account2.transfer(account1, 50.0)

    # Extrato
    account1.extract()
    print('*'*40)
    account2.extract()

except DomainException and AttributeError as e:
    print(e)
