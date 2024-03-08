# def count_digits(n):
#     count=0
#     x=n
#     while(x!=0):
#         x=x//10
#         count+=1

#     return count




# n=int(input())
# print(count_digits(n))

# def count_digits(str):
#     return len(str)

# str=input()
# print(count_digits(str))




# import math
# def count_digits(n):
#     digits=math.floor(math.log10(n)+1)
#     return digits

# n=int(input())

# print(count_digits(n))



# def rvrse(n):
#     revrse=0
#     temp=n
#     while(n!=0):
#         last=n%10
#         revrse=revrse*10+last
#         n=n//10
#     return revrse

# n=int(input())
# print("The reverse number",n ,"is",rvrse(n))

# n=int(input())
# def isp(n):
#     rev=0
#     x=n
#     while(x!=0):
#         last=x%10
#         rev=rev*10+last
#         x=x//10
#     return rev

# # n=int(input())

# Y=isp(n)

# if n==Y:
#     print("palindrome number")
# else:
#     print("Not palindrome number")



# def arm(n):
#     x=n
#     sum=0
#     while(x!=0):
#         last=x%10
#         sum=sum+(last*last*last)
#         x=x//10
#     return sum

# n=int(input())
# if(n==arm(n)):
#     print("Armstrong number")
# else:
#     print("Not Armstrong Number")



# def isprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# n=int(input())

# if n!=1 and isprime(n)==True:
#     print("Prime Number")

# else:
#     print("Not Prime Number")



# from math import sqrt
# def prime(n):
#     for i in range(2,int(sqrt(n)+1)):
#         if(n%i==0):
#             return False
#     return True

# n=int(input())

# if n!=1 and prime(n)==True:
#     print("Prime Number")
# else:
#     print('Not Prime Number')


# def div(n):
#     print("The divisors of ",n, "are:")
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i,end=" ")

# n=int(input())
# div(n)


# from math import sqrt
# def div(n):
#     # lst=[]
#     print("The divisors of",n,"are:")
#     for i in range(1,int(sqrt(n)+1)):
#         if(n%i==0):
#             print(i,end=" ")
#             # lst.append(i)

#             if(i!=n//i):
#                 print(int(n//i),end=" ")
#                 # lst.append(int(n//i))

#     # lst.sort()
#     # return lst

# n=int(input())
# # print(div(n))
# div(n)

# def gcd():
#     a=4
#     b=8
#     ans=1
#     for i in range(1,min(a,b)+1):
#         if(a%i==0 and b%i==0):
#             ans=i
#     print(ans)

# gcd()

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

# print(gcd(20,890))