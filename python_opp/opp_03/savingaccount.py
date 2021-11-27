class BankAccount:
    minimum_balance = 50000

    def __init__(self, account_number, account_name, balance):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")
class SavingAccount (BankAccount):
    monthly_interest_rate = 0.005
    def calculate_interest(self):
        return (self.balance * SavingAccount.monthly_interest_rate)
class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
    def __repr__(self):
        return f"Customer(Tên: {self.name}, Date_of_birth {self.date_of_birth}, Email:{self.email}, Phone: {self.phone})"
saving = SavingAccount('19066666611', 'Tuyen', 510000)
saving.display()
saving.calculate_interest()
c = Customer('Tuyen','12/12/1994','tuyen@amc.com','01122335544')
print(c)