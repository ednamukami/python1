class BankAccount:

    def __init__(self,accountNumber,amount):
        self.acccountNumber=accountNumber
        self.amount=amount

   
    def accountNumber(self):
        return f"The amount has been sent to {self.acccountNumber}" 

    def money(self):
        return f"Your balance is {self.amount}"



