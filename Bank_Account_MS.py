####  Bank Account Management System   ####
class Bankaccount:
    """Banking system"""
    bank_name="HDFC bank"
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        message="   Welcome to HDFC bank  "
        print("Your bank name is = ",self.bank_name)
        print("Your name is  = ",self.name)
        print("Your total balance is = ",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your updated balance is = ",self.balance)
    @classmethod
    def change_bank_name(cls,new_bank_name):
        cls.bank_name=new_bank_name
        print("Your new bank account name is = ",cls.bank_name)
    @staticmethod
    def welcome():
        print("     Thanks to visit our bank   ")
print(Bankaccount.__doc__)
s1=Bankaccount("Amit",5000)
s1.display()
print("Amount after deposit")
s1.deposit(500)
s1.change_bank_name("SBI")
s1.welcome()
s2=Bankaccount("Ram",6000)
s2.display()
print("Amount after deposit")
s2.deposit(600)
s2.change_bank_name("SBI")
s2.welcome()
