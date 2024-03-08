# import re

# def check_password(password):
#     # Rule 1: Check password length
#     if len(password) < 6 or len(password) > 15:
#         return False

#     # Rule 2: Check for at least one capital letter, one digit, and one special symbol
#     if not re.search(r"[A-Z]", password) or not re.search(r"\d", password) or not re.search(r"[*@#]", password):
#         return False

#     return True

# # Prompt the user to enter a password
# password = input("Enter a password: ")

# # Check if the password is valid
# if check_password(password):
#     print("Valid password")
# else:
#     print("Invalid password")


# c) Given a number n, write an efficient function to print all unique prime factors of n. For example, if 
# the input number is 315, then output should be "3 5 7"

n=int(input("Enter Number:"))
lst=[]
k=0
def IsPrime(n):
    for i in range(1,n//2):
        if(n%i==0):
            lst.append(i)

IsPrime(n)
count=0
print(lst)
def chcPF(lst):
    for i in range(2,lst[k]):
        if(lst[k]%i==0):
            count+=1
            k+=1
        
        if(count<=2):
            print(i,end=" ")
        
chcPF(lst)

import math

def print_unique_prime_factors(n):
    # Check if n is a positive integer greater than 1
    if n <= 1:
        return

    # Print all the 2s that divide n
    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    # n must be odd at this point, so a skip of 2 (i.e., i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # While i divides n, print i and divide n
        while n % i == 0:
            print(i, end=" ")
            n = n // i

    # Handle the case when n is a prime number greater than 2
    if n > 2:
        print(n)

# Prompt the user to enter a number
n = int(input("Enter a number: "))

# Print the unique prime factors of n
print("Unique prime factors of", n, "are:")
print_unique_prime_factors(n)
