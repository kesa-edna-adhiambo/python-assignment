# class Account:
#     def __init__(self, number, pin, customer_name):
#         self.number = number
#         self.__pin = pin
#         self.__balance = 0
#         self.customer_name = customer_name

# # outputs the balance when correct pin is given
#     def show_balance(self,pin):
#         if pin == self.__pin:
#             return self.__balance

#         else:
#             return "wrong pin"

# # depositing money to an account
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"{amount} has been deposited in your account.")

# # withdrawing money from an account
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient balance.")
#         else:
#             self.__balance -= amount
#             print(f"{amount} has been withdrawn from your account.")

# # checking balance
#     def check_balance(self):
#         print(f"Hi,{self.customer_name} your Current balance is {self.__balance}.")

# # Method to display the account owner's details and current balance
#     def customer_details(self):
#         print("Name:", self.customer_name)
#         print("Account Number:", self.number)
#         print(f"Balance: {self.__balance}\n")

# # Method to update the account owner's information.
#     def update_customer_details(self, new_name, new_number, new_pin):
#         self.customer_name = new_name
#         self.number = new_number
#         self.__pin = new_pin



class Account:
    def __init__(self,number,pin,account_owner):
        self.number = number
        self.__pin=pin
        self.__balance=0
        self.account_owner=account_owner
        self.transaction_history=[]
    def show_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "wrong pin"
#Method to deposit and withdraw
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"Deposited {amount}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance.")
#Method to display the account owner's details and current balance.
    def view_account_details(self):
        print(f"Account Owner is {self.account_owner} and her balance is {self.__balance}" )
# Method to update the account owner's information.
    def update_customer_details(self, new_name, new_account_number):
        self.customer_name = new_name
        self.account_number = new_account_number
#Method to generate a statement of recent transactions.
    def account_statement(self):
        # print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction}")
#Method to set an overdraft limit for the account.
    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
# Method to calculate and apply interest to the balance.
    #def calculate_interest(self):
        monthly_interest_rate = self.interest_rate / 12
        interest_amount = self.__balance * monthly_interest_rate
        self.__balance += interest_amount
        self.transaction_history.append(f"Interest applied: ${interest_amount}")
#Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        print("Account frozen. No further transactions allowed.")
    def unfreeze_account(self):
        print("Account unfrozen. Transactions can resume.")
#Method to retrieve the history of all transactions made on the account.
    def transaction_history(self):
        return self.transaction_history
#Method to enforce a minimum balance requirement.
    def set_minimum_balance(self, minimum_balance):
        """
        Sets a minimum balance requirement for the account.
        """
        self.minimum_balance = minimum_balance
# Method to transfer funds from one account to another.
    def transfer_funds(self, recipient, amount):
        """
        Transfers funds from this account to another account.
        """
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount:.2f} to {recipient.owner}.")
        else:
            print("Insufficient balance for transfer.")
# Method to close the account and perform necessary cleanup.
    def close_account(self):
        if self.is_open:
            self.is_open = False
            print(f"Account {self.account_number} is now closed.")
        else:
            print("Account is already closed.")






