# r=int(input())
# c=int(input())

# for i in range(1,n+1):
#     if(i%2==1):
#         k=1
#         for j in range(c):
#             print(k,end= "*")
#             k=k+2
#         print()

#     else:
#         if(i%2==0):
#             k=10
#             for j in range(c):
#                 print(k,end="*")
#                 k=k-2
#             print()

# global k
# k=1
# for i in range(1,n+1):
#     for j in range(1,c+1):
#         if(i==1):
#             print(k,end="")
#             k=k+1
#         # else: print(" ")
#         if(j==c): 

#             print(k)
#             k=k+1
        # else:
        # #     print("")
        # if(i==n):
        #     print(k,end="")
        #     k=k+1
        # else:print(" ")
        # if(j==1):
        #     print(k)
        #     k=k+1
        # else:
        #     print(" ")
# d=29
# c=39
# e=11
# for i in range(1,r+1):
#         if(i==1):
#             print(k,end="")
#             k=k+1
#         # print()
#         if(i==r+1):
#              print()
#         elif():
#             print(c)
#             c=c+1
#         elif(i==10):
#             print(k)
#             k=k+1
#         elif(i==10):
#             print(d,end="")
#             d=d-1

# k=1
# n=int(input())
# for i in range(n):
#     for j in range(n):
#             if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#                 print("*", end=" ")
                
#             else:
#                 print(" ", end=" ")
#     print()

# n=int(input())
# k=1
# for i in range(n):
#     # k=k+1
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print(k, end="")
#             k=k+1
#         else:
#             print(" ", end="")
#         # k=k+1
#     print()
# d=1
# k=39
# h=11
# c=30
# for i in range(n):
#     for j in range(n):
#         if(i==0):
#             print(d,end=" ")
#             d=d+1
#     # print()

#         if(j==0 or i==1):
#             print(k,end=" ")
#             k=k-1
#             print()
#         if(j==n-1 or i==1):
#             print(h,end=" ")
#             h=h+1
#             print()
#         if(i==n-1):
#             print(c,end=" ")
#             c=c-1
#         else:
#             print(" ",end="")

# list=[]
# for i in range(5):
#     list.append(int(input()))

# sum=0
# for i in range(5):
#         sum=sum+list[i]

# avg=sum//len(list)

# print(avg)
# n=int(input())
# a=9
# b=9
# sum=0
# for i in range(n):
#     sum+= a*b**1//n

# print(sum)

# 6 ascending order
# lst=[]
# n=int(input())
# # lst=list(map(int,input().split()))
# for i in range(n):
#     lst.append(int(input()))

# lar=lst[0]
# for i in range(1,len(lst)):
#     if(lst[i]>lar):
#         lar=lst[i]

# print("largest element:",lar)
# sml=lst[0]

# for i in range(1,len(lst)):
#     if(lst[i]<sml):
#         sml=lst[i]
# print("Smallest element :",sml)


# str=list(input())
# sr=''.join(str)
# print(sr[::-1])

# s1=frozenset({1,2,3})
# s2={1,2,3,4,5}
# s2.add(s1)
# print(s2)


# Write a program that generates a set of odd numbers and 
# prime numbers in range(1,20) demonstrate the result of union , intersection, -,^ on sets 

# s1={x*2+1 for x in range(0,10) }

# print(s1)

# primes=set(s1)

# for i in range(2,20):
#     j=2
#     flag=0
#     while j<=i/2:
#         if i%j==0:
#             flag=1
#         j+=1
#     if flag==0:
#         primes.add(i)

# print(primes)
# print("Union:",s1.union(primes))
# print("intersection=",s1.intersection(primes))
# print(s1.difference(primes))
# print(s1.symmetric_difference(primes))

# one set in range(1,10) even  and composite in range(1,20)

# issyperset() sum(),len() on sets

# s1={x for x in range(1,10) if x%2==0}
# print(s1)

# s2= {  }

# for i in range(2,20):
#     j=2
#     if(i%j==0):


# Write a program that creates two sets squares and cubes in range(1,10) demonstrate use update pop 
# remove and add,clear 

# s1={x**2 for x in range(1,10)}
# print(s1)
# print(len(s1))
# s2={x**3 for x in range(1,10)}
# print(s2)

# (s1.update(s2))
# print(s1)

# n=int(input())
# set1={x for x in input().split()}
# m=int(input())
# set2={x for x in input().split()}

# print(len(set1|set2))

# n=int(input())
# set1={x for x in input().split()}
# m=int(input())
# set2={x for x in input().split()}
# set3={}
# {set1.symmetric_difference_update(set2)}

# # set1=list((set1))
# list(set1).sort()
# for i in set1:
#     print(i)


# n=int(input())
# count=1
# set={x for x in input().split()}
# set1=list((set))
# for i in set1:
#     for j in set1:
#         if(i==j):
#             count=+1

#     if(count<=1):
#         print(i)

# n=int(input("Enter no of elements:"))
# lst=[]
# for i in range(n):
#     lst.append(int(input()))
# print(lst)
# # lst.sort()

# print(lst)



# #################################


# lst=list(map(int,input().split()))

# n=len(lst)

# for i in range(n):
#     for j in range(n-i-1):
#         if(lst[j]>lst[j+1]):
#             lst[j],lst[j+1]=lst[j+1],lst[j]


# print("Ascending order:",end=' ')

# for i in lst:
#     print(i,end=" ")
# print()

# for i in range(n):
#     for  j in range(n-i-1):
#         if(lst[j]<lst[j+1]):
#             lst[j] , lst[j+1] = lst[j+1] , lst[j]

# print("Descending order:",end=' ')
# for i in lst:
#     print(i,end=' ')

# ######################################

# import math

# numbers=list(map(int,input().split()))

# n = len(numbers)

# AM = sum(numbers) / n

# print("Arithmetic mean:",AM)



# GM = math.prod(numbers) ** (1/n)

# print("Geometric mean:",GM)


# HM = n / sum(1/x for x in numbers)

# print("Hormonic Mean:",HM)

# #####################   HCF/////////////////


# lst=list(map(int,input().split()))

# lst1=[]
# lst2=[]
# for i in range(1 , lst[0]+1):
#     if((lst[0] % i) == 0):
#         lst1.append(i)

# for i in range(1,lst[1]+1):
#     if((lst[1] % i) == 0):
#         lst2.append(i)

# lst1.sort()
# lst2.sort()
# maxi=1
# for i in lst1:
#     for j in lst2:
#         if(i==j):
#             maxo=max(i,maxi)

# print("HCF:",maxo)
# LCM=lst[0]*lst[1]//maxo
# print("LCM:",LCM)

# /////// LCM ////////////

# lst=list(map(int,input().split()))

# n=int(input())

# notes=(n//500) 
# print(n//500 ,"*","500")

# (n%500)//200 
# print((n%500)//200,"*", "200")


# (n%200)//100 
# print((n%200)//100,"*","100")


# (n%100)//50 
# print((n%100)//50,"*","50")

# (n%50)//20 
# print((n%50)//20,"*","20")


# sum=0
# while(n>0):
#     last=n%10
#     sum+=last
#     n=n//10
# print(sum)
# sum1=0
# if(sum>=10):
#     while(sum>0):
#         last=sum%10
#         sum1=sum1+last
#         sum=sum//10

# if(sum1==10):
#     print("10")
#     print("1")
# else:
#     print(sum1)


# n=int(input())

# def prime(n):
#     for i in range(2,n//2+1):
#         if(n%i==0):
#             return False
#         else:
#             return True
# rev=0    
# re=n
# while(re>0):     

#     last=re%10
#     rev=rev*10+last
#     re=re//10

# print("reverse of number:",rev)


# print(prime(n))
# print(n,"is a prime number")

# print(prime(rev))
# print(rev,"is prime number")



# def summ(n):
#     sum=0
#     while(n>0):
#         last=n%10
#         sum+=last**2
#         n=n//10
#         print(sum)
#         if(sum==1):
#             print("Happy number")
#         else:
#             summ(sum)
#             print("Unhappy number")

# summ(n)




# ///   HAPPY NUMBER/////
# x=int(input("Enter Number:"))
# l=[]
# while True:
#     s=0
#     while x>0:
#         s+=(x%10)**2
#         x//=10
#     print(s)
#     if s==1:
#         print("Happy Number")
#         break
#     else:
#         if s in l:
#             print("Unhappy number")
#             break 
#         else:
#             l.append(s)
#             x=s


# #  /////////////////// STRONG NUMBER //////////////////
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)

# n=int(input("Enter number:"))
# sum=0
# s=n
# while(s>0):
#     last=s%10
#     s=s//10
#     # while(True):
#     sum+=fact(last)

# if(sum==n):
#     print("The number is Strong Number")
# else:
#     print("The number is not a Strong Number")



# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()




# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *
        
# for i in range(1,11):
#     if(i<=5):
#         for j in range(i-1):
#             print(" ",end="")
#         for j in range(5-i+1):
#             print("*",end=" ")
#         print()
#     else:
#         for j in range(10-i):
#             print(" ",end="")
#         for j in range(i-5):
#             print("*",end=" ")
#         print()

# n=input()
# for i in range(len(n)):
#     for j in range(i+1):
#         print(n[j],end="")
#     print()

# for i in range(1,6):
#     k=i
#     for j in range(5-i+1,0,-1):
#         print(k,end=" ")
#         k=k+1
#     print()

# n = int(input("Enter Number: "))
# sum=0
# while(n>0):
#     last=n%10
#     sum+=last
#     n=n//10

# print(sum)



# def number_to_words(num):
#     # Define the word representations for numbers from 0 to 19
#     units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
#             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

#     # Define the word representations for tens from 20 to 90
#     tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#     # Check if the number is within the supported range
#     if num < 0 or num > 9999:
#         return 'Length more than 4 is not supported'

#     # Handle the case for zero separately
#     if num == 0:
#         return units[0]

#     words = []  # List to store the words

#     # Extract thousands place digit and add it to the words list if it's non-zero
#     thousands = num // 1000
#     if thousands > 0:
#         words.append(units[thousands] + ' thousand')

#     # Extract hundreds place digit and add it to the words list if it's non-zero
#     hundreds = (num // 100) % 10
#     if hundreds > 0:
#         words.append(units[hundreds] + ' hundred')

#     # Extract tens and ones digits
#     tens_ones = num % 100

#     # Handle numbers from 1 to 19 directly
#     if tens_ones < 20:
#         if tens_ones > 0:
#             words.append(units[tens_ones])
#     else:
#         # Extract tens digit and add it to the words list if it's non-zero
#         tens_digit = tens_ones // 10
#         if tens_digit > 0:
#             words.append(tens[tens_digit])
        
#         # Extract ones digit and add it to the words list if it's non-zero
#         ones_digit = tens_ones % 10
#         if ones_digit > 0:
#             words.append(units[ones_digit])

#     return ' '.join(words)  # Convert the words list to a string


# num = int(input('Enter a number: '))
# result = number_to_words(num)
# print(f'{num}:{result}')


# a=int(input("enter a number1:"))
# b=int(input("enter a number2:"))

# list1=[x*12 for x in range(1,9)]
# list2=[x*14 for x in range(1,9)]
# # print(len(list1))
# # print(list2)

# for i in range(0,len(list1)):
#         for j in range(i,len(list2)):
#                 if(list2[j]==list1[i]):
#                         print("LCM of 12 and 14 is",list2[j])
#                         break

# str=input()
# i=0
# j=len(str)-1
# flag=0

# while(i<=j):
#     if(str[i]!=str[j]):
#         flag=0
#         print("The word is not a palindrome.")
#         break


#     if(str[i]==str[j]):
#         i=i+1
#         j=j-1
#         flag=1
        
# if flag :
#     print("The word is a palindrome.")


# count=0
# str=input("Enter a string: ")
# list=['a','e','i','o','u','A','E','I','O','U']
# for i in str:
#     for j in list:
#         if(j==i):
#             count=count+1

# print("Number of vowels:",count)

# str1=input("Enter string1:")
# str2=input("Enter string2:")
# a=len(str1)
# b=len(str2)
# str=''
# for i in range(0,a):
#         if(i<2):
#                 str = str + str2[i]
#         else:
#                 str = str + str1[i]
# str =str + " "

# for i in range(0,b):
#         if(i<2):
#                 str = str + str1[i]
#         else:
#                 str = str + str2[i]

# print(str)


# str1=input("Enter string1: ")
# str2=input("Enter string2: ")

# a=len(str1)
# b=len(str2)

# str=''

# for i in range(0,a):
#     if(i<2):
#         str=str + str2[i]
#     else:
#         str=str + str1[i]


# str=str + " "

# for i in range(0,b):
#     if(i<2):
#         str=str + str1[i]
#     else:
#         str=str + str2[i]


# print(str)



'''
Write a Python program to add 'ing' at the end of a givenstring (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.

Test case:
Enter String1: asha                                                                                                     
Enter String2: vijetha                                                                                                  
Enter String3: string                                                                                                   
ashaing                                                                                                                 
vijethaing                                                                                                              
stringly
'''

# str1=input("Enter String1: ")
# str2=input("Enter String2: ")
# str3=input("Enter String3: ")
# def modify(str):
#         if len(str) < 3:
#                 return str

#         elif len(str) > 3:
#                 if( str[-3:] == 'ing'):
#                         return str + 'ly'
#                 else:
#                         return str + 'ing'
# res1=modify(str1)
# res2=modify(str2)
# res3=modify(str3)

# print(res1)
# print(res2)
# print(res3)



'''Maximum frequency character in String

Test case:
Enter a string:else                                                                                                    
The maximum of all characters in  else  is : e

'''


# def find_max_char(string):
#     char_frequency = {}

#     for char in string:
#         if char in char_frequency:
#                 char_frequency[char] += 1
#         else:
#                 char_frequency[char] = 1

#     max_frequency = 0
#     max_char = ''

#     for char, frequency in char_frequency.items():
#         if frequency > max_frequency:
#             max_frequency = frequency
#             max_char = char

#     return max_char


# # # # Test case
# string = input("Enter a string: ")

# res  = find_max_char(string)

# print("The maximum of all characters in", string, "is:", res)





'''Comparing User Input to Evaluate Equality Using Operators

test case 1:
Enter the name of the first fruit:apple                                                                                 
Enter the name of the second fruit:apple                                                                                
apple and apple are the same.

Test case2:
Enter the name of the first fruit:apple                                                                                 
Enter the name of the second fruit:banana                                                                               
apple comes before banana in the dictionary.

Test case3:
Enter the name of the first fruit:banana                                                                                
Enter the name of the second fruit:apple                                                                                
banana comes after apple in the dictionary.
'''


# def compare_fruits(fruit1, fruit2):
#     if fruit1 == fruit2:
#         return f"{fruit1} and {fruit2} are the same."
#     elif fruit1 < fruit2:
#         return f"{fruit1} comes before {fruit2} in the dictionary."
#     else:
#         return f"{fruit1} comes after {fruit2} in the dictionary."


# # Test case 1
# fruit1 = input("Enter the name of the first fruit: ")
# fruit2 = input("Enter the name of the second fruit: ")

# result = compare_fruits(fruit1, fruit2)
# print(result)





''' write a python code for LCM of two numbers


input= enter a number1:12
enter a number2:14
output=                                                                                                  
LCM of 12 and 14 is 84 

'''

# def find_lcm(num1, num2):
#     # Find the maximum of the two numbers
#     max_num = max(num1, num2)

#     # Initialize LCM as the maximum number
#     lcm = max_num

#     while True:
#         # Check if lcm is divisible by both numbers
#         if lcm % num1 == 0 and lcm % num2 == 0:
#             break

#         # Increment lcm by the maximum number
#         lcm += max_num

#     return lcm


# # Test case
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))

# res = find_lcm(num1, num2)

# print("LCM of", num1, "and", num2, "is", res)



# list=[]
# def signup():
#         username=input("Enter username:")
#         if username in list:
#             print("Username already exists:")
#             print("Create a different username:")
#         else:
#             list.append(username)
#         password=input("password:")
#         list.append(password)
    
#         frstname=input("Enter firstname:")
#         list.append(frstname)
#         lastname=input("Enter lastname:")
#         list.append(lastname)
#         email=input("Enter email:")
#         list.append(email)
#         DOB=int(input("Enter date of Birth:"))
#         list.append(DOB)
#         Gender=input("GENDER:")
#         list.append(Gender)

#         return "You have been registered successfully"

# def login():
#         usrname=input("Enter username:")
#         if (usrname in list):
#                 pass
#         else:
#             print("Username not Matching:")
#             print("Please enter correct username:")

#         pasword=input("Enter password:")
#         if pasword in list:
#                 pass



# # print(display())
# def display():
#     print("Welcome to KMIT WEBSITE:")
#     print("Enter credentials:")
#     s=input("Click 1 to signup .Click 2 to login ")
#     if s =="signup":
#         signup()
#     elif s=="login":
#         login()

# print(display())






'''Write a Python function that takes a list of words and return the longest word 
and the length of the longest one.

test case:
input=asha vijetha rajesh                                                             
output=Enter a list element separated by space
Longest word:  vijetha                                                                                                  
Length of the longest word:  7 

'''
# lists=[input().split()]
# def func(lists):
#         maps={}
#         for str in lists:
#                 if str in maps:
#                     maps[str] += 1
#                 else:
#                     maps[str] = 1

#         max_char=''
#         maxfreq=0

#         for char,freq in maps.items:
#                 if maxfreq > freq:
#                       freq=maxfreq
#                       max_chr=char


#         return (max_char,freq)

# res=func(lists)
# print(res)

# def find_longest_word(words):
#     # if not words:
#     #     return "Enter a list element separated by space"

#     longest_word = ""
#     longest_length = 0

#     for word in words:
#         if len(word) > longest_length:
#             longest_word = word
#             longest_length = len(word)

#     return f"Longest word: {longest_word}\nLength of the longest word: {longest_length}"

# # Example usage
# words = input("Enter a list of words separated by space: ").split()
# result = find_longest_word(words)
# print(result)


# dic={'a':'12' ,'b':'123'}
# lic=[1,2,3,4]
# grd=["qkbx"]
# res={key:value for key,value in dic.items() }
# dic.clear()
# d2=dic.copy()
# d2['hdbja']=1234
# d=dict.fromkeys(lic,grd)
# print(d.get(1))
# x=dic.values()
# for i in x:
#         print(list(i))

# dic.clear()
# print(sorted(dic.keys()))

# dict={x:x**3 for x in range(1,10) if x % 2==1}
# print(dict)

# for i in dic:
#         print(dic[i])

# list=[3,2,3,2,2,5,2,3,2,4]
# map={}
# for i in list:
#         count=0
#         for j in list:
#                 if i == j:
#                         count+=1
#         map[i]=count

# for map[i],count in map.items():
#         if count > len(list)//2:
#                 print('Element:',map[i],'count=',count)

# if count < len(list)//2:
#         print("-1")




# cook your dish here
# import math
# from collections import defaultdict,deque
# import io
# import os
# import sys
# import heapq
# input = sys.stdin.readline
# # sys.setrecursionlimit(2000)
# mod=1000000007

# for j in range(int(input())):
# 	# n,k=map(int,input().split())
# 	# q = int(input())
# 	n=int(input().strip())
# 	# la=list(map(int,input().split()))
# 	s=input().strip()
# 	# lans=[]
# 	# l=list(map(int,input().split()))
# 	# la=list(map(int,input().split()))
# 	# lb=list(map(int,input().split()))
# 	four=0
# 	zero=0
# 	star=0
# 	tsum=0
# 	ans=0  
# 	remstar=s.count("*")+1
# 	for i in s[::-1]:
# 		if i=="4":
# 			four+=1
# 			ans=(ans+tsum)%mod
# 		elif i=="0":
# 			zero+=1
# 			tsum=(tsum+(star)*pow(2,star-1,mod)%mod+four*pow(2,star,mod)%mod)%mod
# 		else:
# 			ans=(ans*2)%mod
# 			ans=(ans+tsum)%mod
# 			tsum=tsum*2%mod
# 			tsum=(tsum+(star)*pow(2,star-1,mod)+four*pow(2,star,mod))%mod
# 			star+=1
# 		# print(ans,tsum,star,zero,four)
# 	print(int(ans))

# def calculateCGPA():
#     Roll_no=int(input("Enter Roll No:"))
#     for i in range(1,4):
#         Marks=int(input('Enter Marks:'))

# res= calculateCGPA()
# print(res)


# s={1:23,3:4}
# sorted(s)
# print(s)

# s=input("Enter the String:")
# N=''
# for i  in s:
#     N=N + chr(219-ord(i))

# print("New String:",N)

# list=input().split()
# pos=int(input("Enter pos:"))
# cardname=input()

# if (pos >=len(list)//2):
#     print(len(list)-pos)
# else:
#     print(len(list)-pos-1)

# def func(name2,name1='Karna',name3="Bheema"):
#         print(name1,name2,name3)

# func(name2="Rama")


# def func(f):
#         return f*4

# twice=lambda x:x*2
# print(func(twice(3)))

# lsit=(1,23,4,5)
# lsit1=(2,4,5,3)

# def addition(n):
#         return n+n
# lsit=(1,2,3,4)

# res=map(lambda x,y:x*y,lsit,lsit1)

# print(list(res))

# res=[a*2 for a in lsit if a>2]
# print(res)

# num=list(map(lambda x:x*10,[i for i in range(1,11)]))
# print(num)

# list=[[1,2,3],[4,5,6],[7,8,9]]
# res=[j for i in list for j in i]
# print(res)

# importing functools for reduce()
# import functools
# # initializing list
# l = [1, 3, 5, 6, 2]
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# # print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, l))


# def fun(variable):
#         letters = ['a', 'e', 'i', 'o', 'u']
#         if (variable in letters):
#                 return True
#         else:
#                 return False
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# # using filter function
# filtered = filter(fun, sequence)
# print(list(filtered))

# set methode:add(),update(),pop(),remove(),discard(),clear()
# list methods: append(),insert(),extend(),pop(),remove(),clear(),copy()

# s=set([1,2,3,4,5,6,54])
# s1=set([34,3,5,4,6,7])
# # s.pop()
# # s.discard(4)
# # s.remove(2)
# # s.clear()
# # print(2 in s)
# # print(s)

# print(s1.union(s))
# print(s1.intersection(s))
# print(s1.difference(s))
# print(s1.symmetric_difference(s))

# s1.clear()
# s1.update([23,12])
# print(s1)

# res=list(map(lambda x:x*10,[i for i in range(100) if i %10==0]))
# print(res)

# str="sTRSTRING" 

# print(str.capitalize())
# print(str.center(10,"*"))
# print(str.count("sTR",0,len(str)))
# print(str.find("STR",0,len(str)))
# print(str.index("STR",0,len(str)))
# print(str.endswith("IN",0,len(str)))
# print(str.startswith("sT"))
# print(str.islower())
# print(str.isupper())
# print(str.lower())
# print(str.upper())
# print(str.replace("IN","ST"))
# print(str.strip())

# x,y=[int(i) for i in input().split()]
# print(x+y)

# lst=[1,2,3,5,4]
# lst1=[1,2,3,4,5]
# a=dict(zip(lst,lst1))
# print(a)

# dic={"bd":12,"sdb":345,"egrbrw":234}
# # print(dic)
# # for i in dic.items():
# #         print(i)

# dic["ge"]=31242
# # print(dic)

# # print(dic["bsd"])


# # print(len(dic))

# # li=(1,23,3)
# # # li.append(2)
# # print(li.sort())

# N=int(input("Enter the No.of employee details to be listed:"))
# S1=list(map(str,input("Enter the name ,age,salary,Designation of employee:").split()))
# S2=list(map(str,input("Enter the name ,age,salary,Designation of employee:").split()))
# S3=list(map(str,input("Enter the name ,age,salary,Designation of employee:").split()))

# list=[S1,S2,S3]
# max=0
# min=[]
# for i in list:
#         if "SE" in i:
        
#                 for j in i:
#                         if(type(j)==int):
#                                 if(int(j)>max):
#                                         max=int(j)
#                                         min=i
# # print(min)
# print("Employee Name is :",min[0])



# # list_1=[1,1,1,1]
# # list_2=[]
# # list_3=[]

# # for i in range(len(list_1)+1):
# #     for j in range(i):
# #         list_2.append(list_1[j:i])
# # print(list_2)

# # def subArraySum(arr, n, s): 
# #         for i in range(1,n+1):
# #                 sum=arr[i]
# #                 l=i
# #                 for j in range(i+1,n+1):
# #                         sum=sum+arr[j]
# #                         if(sum==s):
# #                                 return (l,j)

# # arr=[1,2,3,7,5]
# # N=len(arr)
# # s=12

# # print(subArraySum(arr,N,s))


# def subArraySum(arr, n, sum_):

#     for i in range(n):
#         currentSum = arr[i]
#         j = i + 1
#         while j <= n:

#                 if currentSum == sum_:
#                         print("Sum found between")
#                         print("indexes % d and % d" % (i, j-1))

#                         return 1

#                 if currentSum > sum_ or j == n:
#                         break

#                 currentSum = currentSum + arr[j]
#                 j += 1

#         print("No subarray found")
#         return 0

# arr=[1,2,3,7,5]
# n=5
# sum=12

# subArraySum(arr,n,sum)


# Python program to print all
# sublist from a given list

# function to generate all the sub lists

# def sublists(arr):
#         lists=[[]]
#         for i in range(len(arr)+1):
#                 for j in range(i):
#                         lists.append(arr[j:i])
#         return (lists)

# arr=[1,2,3,4,5]
# print(sublists(arr))


# lst=input()
# str=lst.split()
# print(str)

# n=int(input())
# lst=list(map(int,input().strip().split()))[:n]
# print(lst)

# lst.reverse()
# print(lst)
# lst.extend([1,2,3,4,5])
# print(lst)

# lst=[x**2 if x%2==0 else x*2 for x in range(1,11)]
# lst.sort()
# print(lst[::1])
# a=int(input())
# res=[[a, b , a*b] for b in range(1,11)]
# print(res)

# lst=list(range(1,11))
# print(lst[::2])

# l1=input().split()
# l2=int(input().split())
# print(l1,l2)

# l1=[1,2,3,4,5,6,7,8,9,10]
# l=len(l1)

# sum=0
# for i in range(l):
#     sum=sum+l1(i)

# mean=sum//l

# print("arithmetic mean:",mean)

# a=int(input("enter a number"))
# prod=1
# while(a>0):
#     prod=prod*a
#     a=a-1

# print("factorial:",prod)\

# a=int(input("enter the number of elements:"))
# l1=[]
# c=0
# for i in range(a):
#     c=c+1
#     l1.append(int(input("enter number %d:"%c)))


# print("largest number:",float(max(l1)))

# a=int(input("enter the number of elements:"))
# c=0
# l1=[]
# for i in range(a):
#         c=c+1
#         l1.append(int(input("enter number %d:"%c)))

# l1.sort()

# print("numbers in ascending order:",[float(i) for i in l1])


# a=int(input("enter a number:"))
# sum=0
# while(a>0):
#         last=a%10
#         sum=sum+last
#         a=a//10

# print("sum of digits:",sum)


# n=int(input("enter a number:"))
# sum=0
# for i in range(1,n+1):
#         if(i%2==0):
#                 sum=sum+i

# print("sum of even numbers:",end="")
# print(sum)

# a=int(input("enter a number:"))
# print("multiplication table for %d"%a)
# c=1
# for i in range(1,11):
#         print("%d*%d = %d"%a %c %(a*c))
#         c=c+1


import json
jsonp='{"fs":"gdd","shgr":"dgt"}'
jsonpython=json.loads(jsonp)
print(jsonpython)
print(type(jsonpython))
print(jsonpython.get("fs"))