

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def transfer_money(self):
        self.balance = self.balance - self.withdraw
        if self.pin is True:
            print("Transfer authorized")
            return True
        else:
            print("Invalid Pin. Transaction canceled. ")
            return False

    def request_money(self):
        self.balance = self.balance + self.deposit
        if self.pin is True:
            print("Request Authorized")
            return True
        else:
            print("Invalid Pin. Transaction canceled. ")
            return False


''' Driver Code for Task 1 '''

'''user = User("Bob", "1234", "password")
print(user.name, user.pin, user.password)'''

""" Driver Code for Task 2 """

'''user = User("Bob", "1234", "password")
print(user.name, user.pin, user.password)
user.change_name("Bobby")
user.change_pin("4321")
user.change_password("newpassword")
print(user.name, user.pin, user.password)'''

""" Driver Code for Task 3"""

'''user = BankUser("Bob", "1234", "password")
print(user.name, user.pin, user.password, user.balance)'''

''' Driver Code for Task 4 '''

'''user = BankUser("Bob", "1234", "password")
print(user.name, "has an account balance of: ", user.balance)
print(user.name, "has an account balance of: ", user.deposit(1000))
print(user.name, "has an account balance of: ", user.withdraw(500))'''

''' Driver Code for Task 5 '''

user = BankUser("Bob", "1234", "password")
user2 = BankUser("Alice", "4321", "password2")
user2.deposit(5000)
print(user2.name, "has an account balance of: ", user2.balance)
print(user.name, "has an account balance of: ", user.balance)
print("You are transferring $500 to Bob")
print("Authorization required")
input("Enter your PIN: ")
print("Tranfering $500 to Bob")
user2.withdraw(500)
user.deposit(500)
print(user2.name, "has an account balance of:", user2.balance)
print(user.name, "has an account balance of: ", user.balance)
print()
print(" You are requesting $250 from Bob")
print("User Authentication is required... ")
input("Enter Bob's PIN: ")
input("Enter password: ")
print("Bob sent $250 ")
user2.deposit(250)
user.withdraw(250)
print(user2.name, "has an account balance of:", user2.balance)
print(user.name, "has an account balance of: ", user.balance)
