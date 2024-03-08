# n=int(input())

# for i in range(1,n+1):
#     if(i<=n//2):
#         for j in range(2*n-2*i):
#             print(" ",end="") 
#         for j in range(2*i-1):
#             print("*",end=" ")   
#         print()    
#     elif (i>n//2):
#         for j in range(2*i-2):
#             print(" ",end="")
#         for j in range(2*n-2*i+1):
#             print("* ",end="")
#         print()                



# for i in range(1,n+1):
#     if(i<=n//2):
#         for j in range(i):
#             print("* ",end="")
#         print()    
#     elif(i>n//2):
#         for j in range(n-i+1):
#             print("* ",end="")
#         print()        

# for i in range(1,n+1):
#     if(i<=n//2):
#         for j in range(n//2-i+1):
#             print("*",end="")
#         for j in range(2*i-2):
#             print(" ",end="")
#         for j in range(n//2-i+1):
#             print("*",end="")        
#         print()
#     elif(i>n//2):
#         for j in range((2*i-n)//2):
#             print("*",end="")
#         for j in range((n-i)*2):
#             print(" ",end="")
#         for j in range((2*i-n)//2):
#             print("*",end="")
#         print()                  


# for i in range(1,n+1):
#     if(i<=n//2+1):
#         for j in range(i):
#             print("*",end="")
#         for j in range(n-2*i+1):
#             print(" ",end="")
#         for j in range(i):
#             print("*",end="")  
#         print()
#     elif(i>n//2+1):
#         for j in range(n-i+1):
#             print("*",end="")
#         for j in range(2*i-n-1):
#             print(" ",end="")  
#         for j in range(n-i+1):
#             print("*",end="")
#         print()                        

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         for j in range(n):
#             print("*",end="")
#         print()    
#     else:
#         for j in range(n//2-1):
#             print("*",end="")
#         for j in range(n//2):
#             print(" ",end="")
#         for j in range(n//2-1):
#             print("*",end="")
#         print()                    
    

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or j==1 or i==n or j==n ):
#             print("*",end="")   
#         else:
#             print(" ",end="")
#     print()        


# for i in range(0,2*n-1):
#     for j in range(0,2*n-1):
#         top=i
#         left=j
#         right=(2*n-2)-j
#         bott=(2*n-2)-i
#         print(n-min(min(top,bott),min(left,right)),end="")
#     print()   

# for i in range(n):
#     k=ord("A")+i
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()    
    

# for i in range(n):
#     for j in range(2*i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*   ",end="")
#     print()        

# f=open("dict.py","rt")
# # print(f.read())
# # print(f.readline())
# for x in f:
#     print(x)
# f.close()

# f=open("dict.py","a")
# f.write("I AM ARUN")
# f.close()

# f=open("dict.py","r")
# print(f.read())
# f.close()


# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     k=ord("A")
#     for j in range(i):
#         print(chr(k),end="")    
#         k=k+1
#     for j in range(i-1):
#         k=k-1
#         print(chr(k-1),end="")
#     print()    


# import numpy as np

# arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# # for x in arr:
# #  for y in x:
# #     for z in y:
# # 	    print(z)

# for x in np.nditer(arr):

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([152,134,1568,156,154,158])

# # plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(size=1000), hist=False)

# plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

# plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

# plt.show()


# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.poisson(lam=2, size=1000), kde=False)

# plt.show()


# n=int(input())

# for i in range(n):


# list=list(map(int,input().split()))

# def check(k):
#     for i in list1:
#         for j in list1:
#             if(i==j):continue
#             if(i+j==k):
#                 return (i,j)

# def check(k):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if(list[i]==list[j]): continue
#             if(list[i]+list[j]==k):
#                 return ("indices:",i,j,"values:",list[i],list[j])


# n=int(input("Enter target:"))
# list=check(n)
# print(list)