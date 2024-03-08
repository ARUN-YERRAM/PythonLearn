# # n=int(input("Enter rows:"))
# # for i in range(1,n+1):
# #     for j in range(0,n-i):
# #         print(" ",end=" ")
# #     k=1
# #     for j in range(i):
# #         print(k,end=" ")
# #         k=k+1
# #     p=0
# #     for j in range(i-1):
# #         k=i-1-p 
# #         print(k,end=" ") 
# #         p=p+1 
# #     print()        

# # def fun(a,b):
# #     if a>b:
# #         return a
# #     else:
# #         return b    

# # sum=lambda x,y:x+y
# # diff=lambda x,y:x-y

# # print(fun(sum(2,3),diff(2,3)))
# # print((lambda x:x*4)(3))


# # def fun(x):
# #     "function to print a number if it is even or odd"
# #     if(x%2==0):
# #         print("Even")
# #     else:
# #         print("Odd")

# # print(fun.__doc__)
# # fun(3)            

# # from math import sqrt
# # print(sqrt(34))

# # import random
# # i=2
# # while(i>=1):
# #     x= print(random.randrange(1000))
# #     print(x)
# #     if(x!=123):
# #         break


# # nums=[7,2,8,4,11]
# # target=11

# # def two_sum(nums, target):
# #     for i in range(len(nums)):
# #         for j in range(i + 1, len(nums)):
# #             if nums[j] == target - nums[i]:
# #                 return [i, j]
# #     raise ValueError("No two sum solution")


# # def two_sum(nums, target):
# #     num_map = {}
    
# #     for i in range(len(nums)):
# #         complement = target - nums[i]
        
# #         if complement in num_map:
# #             return [num_map[complement], i]
        
# #         num_map[nums[i]] = i
    
# #     raise ValueError("No two sum solution")

# # print(two_sum(nums,target))


# # def two_sum(nums, target):
# #     num_map = {}
    
# #     for i in range(len(nums)):
# #         num_map[nums[i]] = i
    
# #     for i in range(len(nums)):
# #         complement = target - nums[i]
        
# #         if complement in num_map and num_map[complement] != i:
# #             return [i, num_map[complement]]
    
# #     raise ValueError("No two sum solution")

# # nums=[11,7,2,8,4]
# # target=11

# # print(two_sum(nums, target))




# import re


# # line="python and java gives Jython"
# # n=re.search("and java",line)

# # print(n)

# # #  match,    search,  



# # sub,

# # line="she sells sea shells on  sells sea shore"

# # pattern="sells"
# # repl="Ocean"

# # r1=re.sub(pattern,repl,line,2)
# # print(r1)



# #   findall

# #  Syntax:  matchlist=re.findall(pattern,input_string)

# # line="^hello how are you .Welcome to python meta character $"
# # x=re.findall("^ello",line)
# # print(x)


# # line="ccsdcscdcded,8,48,""43768\",728"
# # s1=re.findall("\d\d\d\d\d?",line)
# # print(s1)

# # finditr.

# # input_string="LX1 2014 VD1 2015 PDX 20164 Maruti Suzuki cars in India"
# # print("[a,zA-Z]+[\d]+",input_string)

# # Write a program that replaces ; , - , from input string  with a blank space character.

# # str="ASD;1628-1026- ssdc;27377;-387932"
# # x=re.sub(r"[^\D]"," ",str)
# # print(x)



# # x=re.findall(r"\d{2}-\d{2}-(\d{4})","arun.yerram12022005@gmail.com")
# # print(x)

# # WAP That words starts with vowel.

# # x=re.findall(r'\b[aeiou]\w',"arcdfre")
# # print(x)

# # Write a program taht validates a mobile phone  number that number shuld start with 7,8,9 followed by nine digits

# # d1=['7896554321']
# # r1=re.findall(r'[7-9]{1}[0-9]{9}',d1)
# # print(r1)
# # if r1:
# #     print("valid")
# # else:
# #     print("Not Valid")


# #usingfinditer()

# import re
# # pattern=r"[a-z A-Z]+ \d+"
# # matches=re.finditer(pattern,"Lx1 2013,VD1 2015, VDX 20204, Maruti cars")
# # for match in matches:
# #     print("match found at starting index:",match.start())
# #     print(match.end())
# #     print(match.span())
# #     print(match,end=" ")


# str="Peter likes to \n roam on the road at night "
# # # re1=re.I(str,"sfd")
# # # print(re1)
# # res=re.search(".",str)
# # print(res.group())
# # res=re.search(".*",str)
# # print(res.group())

# # tstr="The price of PINEAPPLE is 20"
# # res=re.search(r"(\b[A-Z]+\b).+(\b\d+)",tstr)
# # print(res.groups())
# # print(res.groups(1))
# # print(res.groups(2))




# # CREATE EMPTY TUPLEWITH ELEMENTS
# # creta tuple single element
# # create only one single element ,access element from tuple and also for loop
# # OPERATIONS ON TUPLE :
# # FIND LENGTH ,CONCATENATION btewen two tuples,slicing 
# # repetitionmembership operator in ,not in
# # max min element of tuple
# # convert str to a tuple and list to a tuple
# #  

# tup=()
# tp=(1,)
# tple=(1,2,3)
# for x in tp:
#     print(x)

# print(len(tp))
# print(tp+tple)      
# print(tple[::1])
# print( 1 in tp)
# print(max(tple))
# print(min(tple))

