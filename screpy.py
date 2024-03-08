# n=int(input())
# count=0
# while(n>0):
#     l=n%10
#     if(l==4):
#         count+=1
#     n=n//10

# print(count)

# n=int(input())

# if(n<10):
#     print("Invalid Input")

# else:
#     sr=str(n)
#     for i in range(len(sr)):
#         k=abs(int(sr[0])-int(sr[len(sr)-1]))

#     print(k)

# A,B,N=map(int,input().split())

# for i in range(1,N+1):
#     if(i%2==1):
#         A=A*2
#     else:
#         B=B*2


# sum=A+B
# print(sum)

# from math import gcd

# def reduce_recipe(ingredients):
#     # Find the greatest common divisor (gcd) of all ingredient quantities
#     common_divisor = ingredients[0]
#     for ingredient in ingredients[1:]:
#         common_divisor = gcd(common_divisor, ingredient)
    
#     # Divide each ingredient quantity by the gcd to get the reduced recipe
#     reduced_recipe = [ingredient // common_divisor for ingredient in ingredients]
#     return reduced_recipe

# # Read the number of ingredients
# N = int(input())

# # Read the quantities of each ingredient
# ingredients = list(map(int, input().split()))

# # Reduce the recipe and print the quantities of each ingredient
# reduced_recipe = reduce_recipe(ingredients)
# print(*reduced_recipe)

# N=int(input())
# EC=0
# OC=0
# lst=list(map(int,input().split()))
# for i in range(len(lst)):
#     if lst[i]%2==0:
#         EC+=1
#     else:
#         OC+=1

# print(EC,OC)


# n=int(input())
# m=int(input())

# print("All positions changes in the year ",n)
# n=n+60
# print("All positions changes in the year ",n)



# n,m=map(int,input().split())
# c2=0
# for i in range(n,m+1):
#     c1=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             c1+=1
#     if(c1==4):
#         c2+=1
# print(c2)

# Sample Output 1:
# bbb*bbb
# bb*i*bb
# b*iii*b
# *******

# Sample Input 2:
# 5

# Sample Output 2:
# bbbb*bbbb
# bbb*i*bbb
# bb*iii*bb
# b*iiiii*b
# ********* 

# n=int(input())
# for i in range(n):
#     for j in range(n-1-i):
#         print("b",end="")
#     for j in range(1):
#         print("*",end="")
#     for j in range(2*i-1):
#         if(i==n-1):
#             continue
#         print("i",end="")
#     if(i!=0):
#         for j in range(1):
#             if(i==n-1):
#                 for k in range(0,2*n-2):
#                     print("*",end="")
#             else:
#                 print("*",end="")

#     for j in range(n-i-1):
#         print("b",end="")
#     print()
        

# def generate_series(n):
#     series = [30]  # Initialize the series with the first term

#     for i in range(1, n):
#         if i % 4 == 0:
#             # Every fourth term is the sum of the previous term and 17
#             term = series[i - 1] + 17
#         elif i % 4 == 1:
#             # Every fifth term is the sum of the previous term and 23
#             term = series[i - 1] + 23
#         elif i % 4 == 2:
#             # Every sixth term is the sum of the previous term and 14
#             term = series[i - 1] + 14
#         else:
#             # All other terms are the sum of the previous term and 7
#             term = series[i - 1] + 7
        
#         series.append(term)

#     return series

# # Read the value of N from input
# N = int(input())

# # Generate the series till the Nth term
# series = generate_series(N)

# # Print the series separated by commas
# print(*series, sep=' ')


# def generate_series(n):
#     series = [30]  # Initialize the series with the first term

#     for i in range(1, n):
#         if i % 3 == 0:
#             term = series[i - 1] + 7
#         elif i % 3 == 1:
#             term = series[i - 1] + 5
#         else:
#             term = series[i - 1] + 3

#         series.append(term)

#     return series

# # Read the value of N from input
# N = int(input())

# # Generate the series till the Nth term
# series = generate_series(N)

# # Print the series separated by commas
# print(*series, sep=' ')

# 20 60 104 152 204 260 320 384 452 524 

# n=int(input())

# lst=[]

# lst.append(20)
# for i in range(n):
#     if(i<2):
#         lst.append(lst[0]+40*(i+1)+4*i)
#     else:
#         lst.append(lst[0]+40*(i+1)+4*(2*(i+2)))

# print(lst)

# lst=["Ford","BMW","audi","Benze"]
# def myfun(e):
#     return len(e)

# lst.sort(reverse =True)
# print(lst)

# lst=list(map(int,input().split()))
# lst.sort(reverse=True)
# print(lst[1])
