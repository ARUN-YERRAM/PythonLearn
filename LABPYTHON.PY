# 1.A

# import math

# N = int(input("Enter number of blocks: "))

# V1 = int(input("Enter walking velocity: "))

# V2= int(input("Enter cab velocity: ")) 
# Walk_time = math.sqrt(2)* N/V1

# Cab_time = 2* N/V2

# if (Walk_time<Cab_time): print("Walk") 
# else: print("Cab")


# 1.b

# import math

# x1=int(input())
# y1=int(input()) 

# u=int(input("UP: "))

# y2=y1+u 
# d=int(input('Down:'))

# y2=y2-d

# l=int(input("LEFT: "))

# x2=x1-l
# r=int(input("RIGHT: "))

# x2=x2+r

# dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(int(round (dist,0)))


# # 2.a
# def isPrime(x):
#     f=0
#     for i in range(2,x):
#         if x%i==0:
#             f=1
#             break
#     if f==0:
#         return True
#     else:
#         return False

# n=int(input())
# for i in range(2,n+1):
#     if n%i==0:
#         if isPrime(i):
#             print(i)


# 2.B)

# n=int(input())
# t=n
# s=0
# while(n>0):
#     d=n%10
#     s=s+d
#     n=n//10

# if(t%s==0):
#     print("Yes")
# else:
#     print("No")


# 2.C)

# def isPrime(x):
#     f=0
#     for i in range(2,x):
#         if x%i==0:
#             f=1
#             break
#     if f==0:
#         return True
#     else:
#         return False

# n=int(input())
# for i in range(2,n+1):
#     if n%i==0:
#         if isPrime(i):
#             print(i)


# 2.D)
# def isPrime(x):
#     c=0
#     for i in range(2,x):
#         if x%i==0: c+=1
#     if c==0: return True
#     else: return False

# n=int(input())
# l=[]
# spl=[]

# for i in l:
#     for j in l:
#         if i!=j and i+j<=n and i+j not in spl:
#             spl.append(i+j)

# print(spl)
# if n in spl:
#     print("Yes")
# else:
#     print("No")

# 3.A)

# import re
# s=input()
# n=len(s)
# m1=re.search('[@$#]',s)
# m2=re.search('[^@$#A-Za-z0-9]',s)
# m3=re.search('[A-Z]',s)
# m4=re.search('[a-z]',s)
# m5=re.search('[0-9]',s)
# if(n>=6 and n<=15 and m1 and (not m2) and m3 and m4 and m5):
#     print('Valid')
# else:
#     print('Invalid')


# 3.B)

# str1=list(input())
# str2=str1[::-1]
# for i in range(len(str1)):
#     if str1[i]=='.':
#         if str2[i]=='.':
#             str1[i]='a'
#         else:
#             str1[i]=str2[i]
# s=''
# for i in str1:
#     s += i
# if s==s[::-1]:
#     print(s)
# else:
#     print("Not possible to make Palindrome")

# 3.C)

# import re
# s=input()
# p1='[a-z0-9]'
# p2='\d+'
# if re.search(p1,s):
#     m=re.findall(p2,s)
#     max=int(m[0])

#     for i in m:
#         if int(i)>max:
#             max=int(i)
# print(max)


# 4.A)

# l=[int(x) for x in input().split()]
# n=[i if i in l else -1 for i in range(max(l)+1)]
# print(n)


# 4.B)

# l=[int(x) for x in input().split()]
# n=l[::-1]
# l1=[l[i]+n[i] for i in range(len(l))]
# print(l1)

# 4.c)

# A = [int(i) for i in input().split()]
# temp=A.copy()
# count = 0
# while A != list(sorted(temp)):
#     l=A.copy()
    
#     for i in range( len(A) ):
#         min1 = A.index(min(l))
#         l.remove(A[min1])
#         min2 = A.index(min(l))
        
#         if( min2  < min1 ):
#             last = A[ min2 ]
#             A.remove(A[min2])
#             A.append(last)
#             count+=1
#             break
# print(count)



# # 5.A)


# def lower_triangle(l):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i < j:
#                 l[i][j]=0
# n=int(input())
# mat=[]

# for i in range(n):
#     l=list(map(int,input().split()))
#     mat.append(l)

# lower_triangle(mat)
# for i in range(len(mat)):
#     print(mat[i])



# # 5.B)

# def spiral(si,ei,l):
#     j=si
#     for i in range(si,ei+1):
#         print(l[i][j],end=' ')
        
#     for j in range(si+1,ei+1):
#         print(l[i][j],end=' ')
        
#     for i in range(ei-1,si-1,-1):
#         print(l[i][j],end=' ')
        
#     for j in range(ei-1,si,-1):
#         print(l[i][j],end=' ')

# n = int(input())
# mat=[]
# for i in range(0,n):
#     l = list(map(int, input ().split ()))
#     mat.append(l)
# s=0
# e=len(mat)-1
# while s<e:
#     spiral(s,e,mat)
#     s+=1
#     e-=1


def func(mat):
    r=len(mat)
    c=len(mat[0])

    ans=[]

    top=0
    left=0
    right=c-1
    bottom=r-1

    while(left <=right and top<=bottom):
        for i in range(top,bottom+1):
            ans.append(mat[i][left])
        left+=1

        for i in range(left,right+1):
            ans.append(mat[bottom][i])
        bottom-=1

        if (left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(mat[i][right])
            right-=1

        if (top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(mat[top][i])
            top+=1

    return ans

# mat=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [14,13,16,15]]

# ans=func(mat)

# print(ans)


# 6.A)

# def printDict():
#         n=int(input("Enter a Number:"))
#         d=dict()
#         for i in range(1,n+1):
#             d[i]=i**2
#         print("The Resultant dictionary is")
#         print(d)
# printDict()



# 6.B)


# scores = [int(x) for x in input().split()]
# k=int(input())
# unique_scores=set(scores)
# freq=dict()
# for s in unique_scores:
#     freq[s]=scores.count(s)
# freq2 = dict(sorted(freq.items(),reverse =True, key = lambda kv:(kv[1], kv[0])))

# top_scores=list(freq2.keys())

# print(*top_scores[:k])

