# print("Enter list elements:")
# lists=[]
# for x in range(8):
#     lists.append(int(input()))
    
# nelist=[]

# for x in lists:
#     if(x%2==0):
#         y=x+3
#         nelist.append(y)
# print("New list after adding 3")
# print(nelist)

# nlist=[]
# for x in lists:
#     if(x>7):
#         x=x**2
#         nlist.append(x)
        
# print("New list with squared elements:")
# print(nlist)

# wlis=[]

# for x in lists:
#     if(x<0):
#         wlis.append(-1*x)
        
# print("New list with Positive elements")
# # print(wlis)

# l=list(map(int,input("Enter list elements:").split()))
# x=int(input("Enter search Key:"))

# count=0

# for i in l:
#     if(x==i):
#         count=count+1

        
# if(count==0):
#     print(x," does not exist")
# else:
#     print(x," exists,count of",x,"is",count)
    

# l.sort()
# print("Laregest element:",l[-1])
# print("smallest element:",l[0])

# l=list(map(int,input("Enter list elements:").split()))
# x=int(input("Enter search key:"))

# count=0

# for i in l:
#     if(x==i):
#         count=count+1

        
# if(count==0):
#     print(x," does not exist")
# else:
#     print(x,"exists, count of",x,"is",count)
    

# l.sort()
# print("Laregest element:",l[-1])
# print("smallest element:",l[0])

# l=list(map(int,input("Enter list elements:").split()))

# print("List before interchange:",l)
# k=l[0]
# l[0]=l[-1]
# l[-1]=k
    
# print("List after interchange:",l)
    

# l=[]
# for i in range(3):
#     name=input()
#     age=int(input())
#     marks=int(input())
#     l.append(name,marks,age)
# print(tuple(l))

# Tuple input taking

# t=tuple(input().split())
# print(t)

# t=tuple(int(a) for a in input().split())
# print(t)
# for i in t:
#     print(i)

# t=(1,2,3,8,7)
# print(t.count(2424))
# print(t.index(3,1,6))
# l=[4,5,6,7,8]
# x=tuple(zip(t,l))
# print(x)
# print(divmod(6,6))

# """  Write a program that has two sequences 
# first sequencs stored some qsnx znd second answers use
#  zip function to from valid qustn and asnwers series """

# t=("My name is :","AGE:","Weight:")
# l=("ARUN",18,60)
# print(tuple(zip(t,l)))

# Ques=["Roll_no","Name","Course"]
# Ans=[7,"ARUN","CSD"]
# for q,a in zip(Ques,Ans):
#     print("What is your ",q,"?")
#     print("My",q, "is",a)

# Write a program that scans an email address and forms
# an tuple of user name and domain

# l=["arunyerram12022005@gmail.com","Lucifer2324@gmail.com"]
# for i in l:   print(tuple(i.split('@')))

# t=(1,2,3)
# l=(1,2,3,4)
# x=t+l
# print(x)

# Write a program to prepare topper name his marks in four 
# subjects wher marks specified as list in tuple

# list=[["ARUN","ARJUN"],[75,75,60,60]]
# print(t[0])
# print


# s={1,2,3,(4,5,5)}
# print(s)
# print(type(s))
# t=set([1,2,3,4,5])
# print(t)

# s={a for a in range(5) if a%2==0}
# print(s)

# Write a program that has nested list of  details edit and print it.

# del s
# print(s)


# x=input("Enter somme text:")
# x={a for a in x.split(",")}
# print(x)

s={1,2,3}
print(s)