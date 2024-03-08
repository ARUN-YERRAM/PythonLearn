# x=input('Enter text:')
# x={a for a in x.split(",")}
# print(x)

# s={1,2}
# # t=s
# # print(t)
# s.add(23)
# t=s.copy()
# s.add(345)
# print(s,t)

# s={1,2,3,45}
# t={1,2,4,3,5,45,6,}
# print(s.difference(t))

# x={"a","d","c"}
# y={"d","c","a","k"}
# z={"a","f","g","j"}

# (z.intersection_update(x,y))
# print(z)

# lst=set(map(int,input().split()))
# print('list elements:')
# print(lst)

# n=int(input("Enter rows:"))

# for i in range(1,n+1):
#     if(i%2==1):
#         res=1
#     else:
#         res=0

#     for j in range(i):
#             print(res,end=" ")
#             res=1-res
#     print()


# for i in range(1,n+1):
#     if(i<=(n//2)+1):
#         for j in range(n-2*i+1):
#             print(" ",end="")
#         for j in range(2*i-1):
#             print("*",end=" ")
#         print()
#     else:
#         for j in range(2*i-n-1):
#             print(" ",end="")
#         for j in range(2*n-2*i+1):
#             print("*",end=" ")
#         print()

# list=[float(a) for a in input().split()]
# list=list(map(float,input().split()))
# lss=[]
# for i in list:
#     lss.append(abs(i))

# sum=0
# for i in lss:
#     sum+=i
# sum1=sum//len(list)
# print(float(sum1))


# str=input()
# wrds=str.split()
# revrsedwrds=' '.join(reversed(wrds))
# print(revrsedwrds)


# k=1
# for i in range(5):
#     for j in range(i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# list=[123,24,565,6,76,8,93,45746,746,4675676]
# list.sort()
# print('max:',list[0])
# print('min:',list[-1])

# n=int(input("N = "))
# arr=list(map(int,input("\'ARR=\'").split()))

# arr.sort()
# print(arr[-1])

# import math
# x1=int(input())
# y1=int(input())

# u=int(input("Enter up:"))
# y2=y1+u

# D=int(input("Enter Down:"))
# y2=y2+D

# L=int(input("ENter left:"))
# x2=x1-L

# R=int(input("Enter Right:"))
# x2=x2+R

# dist=math.sqrt((x2-x1)**2+(y2-y1)**2)

# print(int(round(dist,0)))


# strg=""
# for i in range(1,101):
#     if(i%3==0):
#         strg=strg+"Fizz"
#     if(i%5==0):
#         strg=strg+"Buzz"
#     else:
#         strg=strg+str(i)
#     print("\n")