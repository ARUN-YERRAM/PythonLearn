# from flask import Flask ,render_template,request
# print("Ok!") 

# import re
# pattern = re.compile(r'\d+')
# result = pattern.search("abc123def456")
# print(result)

# import re
# pattern = re.compile(r'[aeiou]')
# result = pattern.search("Hello")
# print(result)

# import re

# pattern = re.compile(r'\d+')
# text = "I have 3 apples, 5 bananas, and 7 cherries."
# matches = pattern.findall(text)
# print(matches)


# import re

# pattern = re.compile(r'\d+')
# text = "I have 3 apples, 5 bananas, and 7 cherries."
# match_iterator = pattern.finditer(text)

# for match in match_iterator:
#     print(f"Match: {match.group()}, Start: {match.start()}, End: {match.end()}")


# import re
# pattern = re.compile(r'\d+', re.MULTILINE)
# text = 'hcrecve2rjhc\ncbkbce4nfjr'
# res = pattern.findall(text)
# print(res)


# s = "geekgeek"
# def fun(s):
#     count = 0
#     while s!="":
#         if "geek" in s:
#             s = s.replace("geek","")
#             if s=="":
#                 count+=2
#             else:
#                 count+=1
#         else:
#             return -1

#     return count

# print(fun(s))


# def check(D, N, A):
#         for i in range(len(A)):
#             j = (i+D)%N
#             def swap(A,i,j):
#                 srt = A[i]
#                 A[i] = A[j]
#                 A[j] = srt
                
#                 return (A[i],A[j])
#             A.append(swap(A,i,j))

#         if A==sorted(A):
#             return "Yes"
#         else:
#             return "No"
# D = 2
# N =4
# A = [3,2,1,5]
# print(check(D, N, A))


# def makeStringEmpty(s):
#     def remove_geek(s):
#         while "geek" in s:
#             s = s.replace("geek", "", 1)
#         return s
    
#     def helper(s):
#         if len(s) == 0:
#             return 0
#         if "geek" not in s:
#             return -1
        
#         min_operations = float('inf')
        
#         for i in range(len(s) - 3):
#             if s[i:i+4] == "geek":
#                 new_s = s[:i] + s[i+4:]
#                 remaining_operations = helper(new_s)
#                 if remaining_operations != -1:
#                     min_operations = min(min_operations, 1 + remaining_operations)
        
#         if min_operations == float('inf'):
#             return -1
        
#         return min_operations

#     result = helper(s)
#     return result if result != -1 else -1

# s = "geekgeekgeek"
# print(makeStringEmpty(s))



# import math
# def check(D, N, A):
#         def gcd(a, b):
#             while b:
#                 a, b = b, a % b
#             return a
    
#         if gcd(D, N) == 1:
#             return True
#         else:
#             return False
# N = 4
# D = 2
# A = [3, 2, 1, 5]

# print(check(D,N,A))


# def printFibb(n):
#         arr  = [1,1] + [0 for i in range(n-2)]
        
#         for i in range(2,n):
#             arr[i] = arr[i-1] + arr[i-2]
        
#         return arr
# n = 5
# print(printFibb(n))



# def isUgly(n):
#     if n <= 0:
#         return False

#     for prime in [2, 3, 5]:
#         while n % prime == 0:
#             n //= prime

#     return n == 1

# print(isUgly(6))  # True (2 * 3)
# print(isUgly(1))  # True (No prime factors)
# print(isUgly(14)) # False (Includes the prime factor 7)


# def sum(n):
#                 dig_sum = 0
#                 while n> 0:
#                     last = n%10
#                     dig_sum += last
#                     n //=10
#                 return dig_sum if dig_sum < 10 else sum(dig_sum) 


# print(sum(729))


# n = int(input())

# if (n & 1) == 0 :
#     print("Even")
# else:
#     print("Odd")

res = 0
arr = [7,4,5,4,3,5,3,6,8,6,8,8,2,2,8,9,9]
for i in range(len(arr)):
    res = res ^ arr[i]

print(res)