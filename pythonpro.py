# import csv
# data="bwhdcb"
# file=open(data)
# dt2=csv.DictReader(file,delimiter=',')
# value=int(input())
# ob1=input("Enter the value \n")
# for val in dt2:
#     if value==1 and val["Roll No"]==ob1:
#         print(val["Name"])
#     if value==1 and val["Name"]==ob1:
#         print(val["RollNo"])


# import numpy as np
# import pandas as pd  

# data = pd.read_csv("Iris.csv")
# display(data)

# print("The mean of Sepal length is",data["sepallengthCm"].mean())
# print("The mean of Sepal length is",data["sepallengthCm"].median())
# print("The mean of Sepal length is",data["sepallengthCm"].std())


# boolcond = (data["Petallength"]>1.5 and data["Sepallength"]<5.0)
# print(data[boolcond])

# import pandas as pd 
# data = pd.read_csv("Iris.csv")
# data.isnull()

# def fun(lists):
#     list_2=sorted(lists)
#     moves=0

#     for i in range(len(lists)):
#         if lists[i]!=list_2[i]:
#             moves+=1
    
#     return moves

# list_1=list(map(int,input().split()))

# res  =   fun(list_1)

# print(res)


# A = [int(i) for i in input().split()]
# temp=A.copy()

# count=0

# while A!=list(sorted(temp)):
#     l=A.copy()

#     for i in range(len(A)):
#         min1 = A.index(min(l))
#         l.remove(A[min1])
#         min2 = A.index(min(l))

#         if min2<min1:
#             last = A[min2]
#             A.remove(A[min2])
#             A.append(last)
#             count+=1
#             break
# print(count)





# APPROACH 1                        TIME COMPLEXITY : O(N*N)
#                                   SPACE COMPLEXITY: O(1)
# list = [1,2,4,2,5,3,5,4,3]
# flag=0
# for i in range(len(list)):
#     for j in range(len(list)):
#         if i!=j and list[i]==list[j]:
#             flag=1
        
#     if flag==0:
#         print(list[i])
#         break

#     flag = 0

# APPROACH 2:               TIME ANA SPACE COMPLEXITY: O(n*logn) ,O(1)

# list_1=[1,2,4,1,5,2,5,4,3]
# list_1.sort()
# for i in range(0,len(list_1),2):
#     if list_1[i]!=list_1[i+1]:
#         print(list_1[i])
#         break


# APPROACH 2:               TIME ANA SPACE COMPLEXITY: O() ,O(n)



# def fun(a,b):
#     return a+b

# a,b = map(int,input().split())

# re = fun(a,b)

# print(re)


# from sympy import *
# x = symbols("x")
# y = Function('y')
# dsolve(Derivative(y(x),x)+y(x)*cos(x)-sin(x)*cos(x))


# def lengthOfLIS(nums):
#     if not nums:
#         return 0

#     n = len(nums)

#     # Initialize an array to store the length of the longest increasing subsequence
#     lis_length = [1] * n

#     # Iterate through the array to compute LIS length
#     for i in range(1, n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 lis_length[i] = max(lis_length[i], lis_length[j] + 1)

#     # The maximum value in the lis_length array represents the length of the LIS
#     return max(lis_length)

# # Example usage:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# print(lengthOfLIS(nums))  # Output: 4 (The LIS is [2, 3, 7, 101])

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
