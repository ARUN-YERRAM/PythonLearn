#  for i  in range(4):
#     for j in range(4):
#         print("#",end=" ")
    # print()

# fruits=["apple","banana","mango",'berry']
# for i in fruits:
#     print(i)
#     for j in i:
#         print(j)
#      print()     

# for i in range(4):
#     for j in range(0,i):
# # #         print("*")

# # r1=['tic','tac','toe']

# # for i in r1:
# #     for j in i:
# #         if(j=='t'):
# #             continue
# #         else:
# #             print(j)
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="")
#     print()   
# for a in range(2,7):
#     for b in range(1,a):
#         print("#",end=" ")
#     print()

# # for i in range(0,5):
# #     print(i)
# # print()    

# # for i in range(0,10):
# #     print(i,end=" ")

# for i in range(0,10):
#     for j in range(0,5):
#         print(j)
#     print()
#     break
# i=0
# for i in range(0,10):
#     print(i,end=" ")   
# k=1 
# j=5
# for j in range(5,0,-1):
#     for i in range(0,j):
#         print(k,end=" ")     
#     print()
#     k=k+1
#     j=j-1

# for i in range(0,5):
# #     for j in range(i):
# #         print("*",end="")
# #     print()    

# k=5
# c=5
# for i in range(0,k):
#     for j in range(0,k):
#         print(c,end=" ")
#     print()
#     c=c-1
#     k=k-1
# n=int(input("Enter no of rows:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()       

# for i in range(0,5):
#     if(i==0 or i==4):
#         for j in range(0,7):
#             print("*",end=" ")
#         print()    
# n=int(input("Enter n:"))
# k=n
# for i in range(n):
#     for j in range(k,0,-1):
#         print("*",end=" ")
#     k=k-1    
#     print()    

# # n=int(input("Enter n:"))
# # k=1
# # for i in range(n):
# #     for j in range(i+1):
# #         print(k,end=" ")
# #         k=k+1    
# #     print()

# n=int(input("Enter n:"))
# for i in range(n+1):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()           
# n=int(input("Enter n:"))
# def pyramid(rows):
#     for i in range(rows):
#         print(''*(rows-i-1)+'*'*(i+1))

# pyramid(n)
# import math

# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)

#     return res

# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element

# if __name__ == '__main__':
#     r = 5 # row number
#     c = 3 # col number
#     element = pascalTriangle(r, c)
#     print(f"The element at position (r,c) is: {element}")

from typing import *

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1) )
        ans.append(tempLst)
    return ans

if __name__ == '__main__':
    n = 10
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
