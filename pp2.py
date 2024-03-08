# def unique(lst):
#     new = []
#     for i in lst:
#         if i not in new:
#             new.append(i)
#     return new

# list = [1,2,3,4,3,2,5,6,4,3,26,7,8,9,7,8,6,56,4,5,6]
# print(unique(list),len(list),sep="\n")

# def fun(**kwargs):
#     return (kwargs,type(kwargs))

# print(fun())

# list = [i for i in range(1,11) if i%2==0]
# print(list)
# for i in range(5):
#     list.append(i)
#     print(list)

# import numpy as np
# import matplotlib.pyplot as plt

# image = np.zeros(3,3,3),dtype=np.uint8
# plt.imshow(image)
# plt.axis('off')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt


# lst = [x for x in input().split()]
# lst.sort()
# print(lst)


# import random
# char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW12345678910!@#$%^&*()"
# password=""
# length=int(input("Enter length:"))

# for i in range(length):
#     password+=random.choice(char)
# print(password)



# list=(1,2,4,5,6,7,8,10)
# lsit = [i if i in list else -1 for i in range(max(list)+1)]
# print(lsit)
# list_1=[i for i in list[::-1]]
# res=[list[i]+list_1[i] for i in range(len(list))]
# print(res)

# def add(n):
#     return n+n
# lis=(1,2,4,5,6,7,8,10)
# res=map(add,lis)
# print(list(res))

# list_1=[1,2,3,4,5]
# list_2=[6,7,8,9,10]

# res=map(lambda x,y:x+y,list_1,list_2)
# print(list(res))

# lst=[[j for j in range(5)] for i in range(3)]
# print(lst)
# lst=list(map(lambda i:i*10, [i for i in range(1,11)]))
# print(lst)

# lst=[123,435,567,8865]
# def dsum(n):
#     dsums=0
#     for i in str(n):
#         dsums+=int(i)
#     return dsums

# nlist=[dsum(i) for i in lst]
# print(nlist)

# A=[[1,2,3],[4,5,6],[7,8,9]]

# res=[[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
# print(res)

# import functools

# # lsi=[1,2,34,5,6,78]

# # res=functools.reduce(lambda a,b:a if a>b else b , lsi)
# # print(res)


# s={1,2,"wf",3.45,2,1,"wf","dbfg",3.453,"fs"}
# # print(list(set(s)))
# # print(len(s))
# # print(dir(s))
# s2={1,2,34,45}
# s.update(s2)
# print(s,len(s))
# s.clear()
# print(s)

# x=160
# print(bin(x))
# print(hex(x))
# print(oct(x))


# def fun(*place):
#     print("I am in",place[2])

# fun("Hyderabad","Pune","Noida")

# def fun(f,n):
#     print(f(n))

# twice = lambda x:x*2
# thrice = lambda y:y*3
# # fun(twice ,3)
# # fun(thrice ,4)

# print(twice(3),thrice(4),sep="\n")

# def fun(n):
#     "Function to check whether given number is odd or even"
#     if n%2==0:
#         print("Even")
#     else:
#         print("ODD")
# x=int(input())
# fun(x)
# print(fun.__doc__)

# import re
# srt = "the humpty dumpty"
# rep="The"
# srch= "humpty"
# print(re.sub(srch,rep,srt))

# import re
# str="Foc67us o5n yoour9sel1f"
# res = re.findall(r"o{1}..",str)
# # for i in res:
# print(res)


# import re
# #Check if the string starts with "The" and ends 
# # with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("YES! We have a match!")
# else:
#     print("No match")

# try:
#     n = int(input())
#     m=int(input())
#     print((m+n)//(m-n))

# except ValueError as e:
#     print("Invalid Value",e)
# except ZeroDivisionError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except Exception as e:
#     print("Error",e)
# finally:
#     print("Code Completed")


# class Solution:

import json
with open("")
