class Account:
    def __init__(self, number, pin, customer_name):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.customer_name = customer_name

# outputs the balance when correct pin is given
    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance

        else:
            return "wrong pin"

# depositing money to an account
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} has been deposited in your account.")

# withdrawing money from an account
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} has been withdrawn from your account.")

# checking balance
    def check_balance(self):
        print(f"Hi,{self.customer_name} your Current balance is {self.__balance}.")

# Method to display the account owner's details and current balance
    def customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.number)
        print(f"Balance: {self.__balance}\n")

# Method to update the account owner's information.
    def update_customer_details(self, new_name, new_number, new_pin):
        self.customer_name = new_name
        self.number = new_number
        self.__pin = new_pin






