# i=0
# while(i<=6):
#     i+=1
#     # if(i%2==0):
#     print("YOU are the Best!")
        
# else:
#     print(i)
        

# i=1
# sum=0
# while(i<=10):
#     sum+=i
#     print(sum)
#     i+=1
# # print(sum)

# print(dict(range(10,1,-1)))

# print(not(2>5))

# S = "dgbgdsd"
# s = S[-1::-1]
# print(id(s))

# S = """cbwdkjc
# cwjcb"""
# print(id(S))

# name =["ARUN" ,"YERRAM"]
# name1 = []
# for i in name:
#     name1.append(i[-1::-1])
# print(len(name1[0]))

# srt = "arunyerram"
# print(srt[::-1])
# # print(srt.capitalize())
# # print(srt.upper())
# # print(srt.lower())
# print(srt.count("r"))
# str = srt.split("a")
# print(str[:])
# print(srt.isupper())

# name = "arunyerram"
# print(name.replace("arun","yerram"))
# print("my name is {}".format(name))
# print(f"my name is {name}")
# print(name*3)
# print("a"*3)

# text = "the quik Brown fox jumps over the lazy dog"
# for i in text:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         print(i,end=" ")

# name = input()
# rev = name[::-1]
# if name ==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# list = [2,3,4,5]
# # print(list)
# # print(type(list))
# # print(len(list))
# # print(list[-(len(list)-1)])


# print(list[::-1])
# list.append(234)
# print(list)
# lst = [342,5,234]
# list.append(lst)
# print(list)

# tol = ([1,2,3],)
# print(tol[:])
# print(id(tol))
# print(tol)
# # print(id(tol[0]))
# a,b=tol
# print(a,b)
# a[0]=123
# print(tol)
# print(tol.index("rahul"))

# for i in tol:
#     print(i)

# t=(1,2,3)
# print(t*tol)

# st = set({1,2,3})
# print(st)
# for i in st:
#     print(i)
# st.add(45)
# st.update("arun",[1,2,3,12,3])
# st.pop()
# print(st)

# st1={1,2,3,4,5,54}
# st1.difference_update(st)
# print(st1)
# for i in st1:
#     print(i)

# sst=set()
# lst=[i for i in range(10) if i%2==0]
# for i in range(len(lst)):
#     sst.add(lst[i])
# print(sst)

# str = "The quick brown fox jumps The the dog quick  over the lazy dog"
# lst = str.split()

# s =set(lst)
# print(s)

# def fun(l):
#     "The function class SST"
#     return l+10
# # num=int(input())
# x=fun(1234)
# fun



def lsearch(lst,trgt):
    count=0
    for i in range(len(lst)):
        count+=1
        if lst[i]==trgt:
            print("Iterations by lsearch:",count)

            return i
    print("Iterations by lsearch:",count)
    return -1
def bsearch(lst,trgt):
    left = 0
    right = len(lst)-1
    count = 0

    while left<=right:
        count += 1 
        mid = (left + right)//2
        if lst[mid] == trgt:
            print("Iterations by binary search:",count)
            return mid
        elif lst[mid] < trgt:
            left = mid+1
        else:
            right = mid - 1
    print("Iterations by binary search:",count)
    return -1

ls= [12,23,43,57,65,78,89,91,99,108,110]
target = 108

res = lsearch(ls,target)

res1 = bsearch(ls,target)

if res!=-1:
    print("Target Index:",res)
else:
    print("Target Index:",res ,".Element not found")

if res1!=-1:
    print("Target Index:",res1)
else:
    print("Target Index:",res1 ,".Element not found")