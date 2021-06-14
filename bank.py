from datetime import datetime

class BankAccount:

    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.statement=[]
        self.loan=0
       
        

    def  show_balance(self):
        return f"Your balance is {self.balance}"

   
    def name(self):
        return f"The amount has been sent to {self.acccountNumber}" 

    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"

        if amount >0:
            self.balance=amount
            
            now=datetime.now()
            transaction1={
                "amount":{amount},
                "time":now,
                "narration":"You have deposited",
            }
            self.statement.append(transaction1)
        return f"Your balance is {self.balance}"
    def show_statement(self): 
        for transation in self.statement:
            amount=transation["amount"]
            narration=transation["narration"]
            time=transation["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}: {narration}: {amount}")
        return             

        return self.statement
    
    def withdraw(self,amount):
        try:
            10+amount
        except TypeError:
            return f"your amount should be in figures"    
        if amount <0:
            return f"your balance is {self.balance} you cannot withdraw"
        else:    
            self.balance=amount
           
        now=datetime.now()
        transaction2={
                "amount":{amount},
                "time":now,
                "narration":"You have withdrawn",
        }
        self.statement.append(transaction2)
        return self.show_balance()    

                     
       

        
    def borrow(self,amount):
        try:
            11+amount
        except TypeError:
            return f"The amount should be in figures"    

        if amount<0:
            return "You are not qualified"
        elif self.loan<0:
            return "You are not qualified"
        elif amount<0.1*self.balance:
            return "You are not qualified"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance
            
        now=datetime.now()
        transaction3={
                "amount":{amount},
                "time":now,
                "narration":"Your loan has been approved you will recieve your account balance shortly",
            }   
        self.statement.append(transaction3)
        return f"You will recieve your account balance shortly"
     

        
    def repay(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount should be in figures"    
        if amount<0:
            return"you have not settled your balance"
        elif amount<=self.loan:
            return "decrease loan with amount"
        elif amount>self.loan:
            difference=amount-self.loan
            self.loan=0
            self.deposit(difference)
          
        now=datetime.now()
        transaction4={
                "amount":{amount},
                "time":now,
                "narration":"Conglaturations ,your loan has been fully settled,your new account balance is {difference}. ",
            }
        self.statement.append(transaction4)
        return f"your loan balance is fully settled your new account balance is {difference}"
            
    def transfer(self,amount,account):
        try:
            10+amount
        except TypeError:
            return f"the amount should be in figures"
        fee=amount*0.05
        total=amount+fee
    
        if amount <0:
            return f"you are not qualified to make the transfer"
        elif total>self.balance:
            return f"your balance is {self.balance} and you need atleast {total} for this transfer"
        else:
            account.deposit(2800000)
            self.balance=total
            return f"the amount has been tansferred to the account number"

class Mobile_moneyAccount(BankAccount):

    def __init__(self, name, phone_number,service_provider):
        BankAccount. __init__(name, phone_number)
        self.service_provider=service_provider

    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount should be in figures"
        if amount<0:
            return f"you have insufficient funds"
        elif amount>self.balance:
            return f"we can not complete the transaction as requested"                       
        else:
            self.balance-=amount
            return f"your request has been successfull you will recieve {amount} shortly"
