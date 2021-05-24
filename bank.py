class BankAccount:

    def __init__(self,name,phonenumber):
        self.name=name
        self.balance=0
        self.phonenumber=phonenumber


    def  show_balance(self):
        return f"Your balance is {self.balance}"

   
    def name(self):
        return f"The amount has been sent to {self.acccountNumber}" 

    def deposit(self):
        return f"Your balance is {self.balance}"
    def deposit(self,amount):
        self.balance+=amount
        return self.show_balance()
    def withdraw(self,amount):
        if amount>self.balance :
            return f"your balance is {self.balance} you cannot withdraw {amount}"
        else:
            self.balance-=amount
            return self.show_balance()
    def borrow(self,amount):
            return f"your request has been confirmed , you have recieved {self.amount}"
    def pay_back(self,amount):
            return f"you are expected to pay back this amount {amount} by 22nd july 2024"
            



