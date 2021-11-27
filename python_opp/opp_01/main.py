class BankAccount:
    def __init__(self,account_number, account_name, balance):
       self._account_number = account_number
       self._account_name = account_name
       self._balance = balance
    def get_account_number(self):
        return self._account_number
    def get_account_name(self):
        return self._account_name
    def get_balance(self):
        return self._balance
    def set_balance(self,new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Giá trị balance không hợp lệ")
    def display(self):
        print("Thông tin tài khoản là:", f"{self.get_account_number()}, {self.get_account_name()}, {self.get_balance()}")
    def withdraw(self,amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            print(self._balance)
        else:
            print("Amount không hợp lệ")
        
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(self._balance)
        else:
            print("Amount không hợp lệ")
        
        
bank = BankAccount("19031566", "TUYEN LE", 3000000)
bank.display()
bank.withdraw(4000000)
bank.deposit(150000)