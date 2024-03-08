a=int(input("1.To create a bank account 2.Have a bank account"))
Total=10000
name=input()
self={}
if(a==1):
    b=int(input("Enter number 1.To withdraw money  or 2.To deposit Money"))
if(b==1):
            deposit(self,name,amount)
else:




# if(b==1):
#     k=int(input("Enter amount to be withdraw:"))
#     Total=Total-k
#     print("You have withdrawn %d amount "%k)
#     print("You have %d amount left in your deposit account"%(Total-k))
# else:
#     A=int(input("Enter amount to be deposited:"))
#     Total+=A
#     print("You have successfully deposited %d amount in your account"%(A))
#     print("You have %d amount


# def __init__(self):
#         self.customers = {}

def create_account(self, name, initial_balance=0):
        if name in self.customers:
            raise ValueError("Customer already exists")
        account_number = generate_account_number()  
        self.customers[name] = Account(name, account_number, initial_balance)

if(a==1):
    create_account(self, name, initial_balance=0)



def get_account(self, name):
        if name not in self.customers:
            raise ValueError("Customer does not exist")
        return self.customers[name]

def deposit(self, name, amount):
        account = self.get_account(name)
        account.deposit(amount)

def withdraw(self, name, amount):
        account = self.get_account(name)
        account.withdraw(amount)

if(b==1):
    deposit(self,name,amount)

def transfer(self, sender_name, receiver_name, amount):
        sender_account = self.get_account(sender_name)
        receiver_account = self.get_account(receiver_name)
        sender_account.withdraw(amount)
        receiver_account.deposit(amount)

class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

def deposit(self, amount):
        self.balance += amount

def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount


import random 
import string

def generate_account_number(min_length, numbers=True, special_characters=True):
    letters= string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers :
        characters += digits
    if special_characters:
        characters += special


    pwd=""
    meets_criteria=False
    has_number=False
    has_special= False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True 
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special   

    return pwd          

min_length = int(input("Enter the minimum length:"))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_account_number(min_length, has_number, has_special)    
print(pwd)