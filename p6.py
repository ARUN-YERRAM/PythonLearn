# """"  A company decides to give a Bonus to all its Employes On diwali .
# 5% bonus on salary to male and 10% to female. Write a program to this while accepting a gender  """

Gen=(input("Enter gender(M,F):"))
salary1=20000
salary2=20000
salary1=salary1 + salary1//20
salary2=salary2 + salary2//10

if(Gen=="M"):
    print(salary1)
elif(Gen=="F"):
    print(salary2)
 