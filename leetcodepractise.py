# list_1=[1,2,3,4,5,6,7,8,9,10]
# k=int(input())
# result=[]
# if (len(list_1)%k==0):
#     for i in range(0,len(list_1)+1):
#         result=result+[i]
#     #print(result)
#     list_3=[]
#     for i in result:
#         if (i%k==0):
#             list_3=list_3+[i]
#     #print(list_3)
#     list_2=list_3[0:len(list_3)-1]
#     #print(list_2)
#     list_4=[]
#     for i in range(0,len(list_2)):
#         list_4=list_4+[[list_2[i],list_3[i+1]]]
#     #print(list_4)
#     list_6=[]
#     for i in list_4:
#         list_5=[]
#         for j in range(min(i),max(i)):
#             list_5=list_5+[j]
#         list_6=list_6+[list_5]
#     #print(list_6)
#     list_8=[]
#     for i in list_6:
#         list_7=[]
#         for j in i:
#             list_7=list_7+[list_1[j]]
#         list_8=list_8+[list_7]
#     #print(list_8)
#     list_9=[]
#     for i in list_8:
#         list_9=list_9+[i[::-1]]
#     #print(list_9)
#     list_10=[]
#     for i in list_9:
#         for j in i:
#             list_10=list_10+[j]
#     #print(list_10)
#     for i in list_10:
#         print(i,end=" ")
# elif (len(list_1)%k!=0 and len(list_1)>=k):
#     for i in range(0,len(list_1)):
#         result=result+[i]
#     #print(result)
#     list_3=[]
#     for i in result:
#         if (i%k==0):
#             list_3=list_3+[i]
#     #print(list_3)
#     list_2=list_3[0:len(list_3)-1]
#     #print(list_2)
#     list_4=[]
#     for i in range(0,len(list_2)):
#         list_4=list_4+[[list_2[i],list_3[i+1]]]
#     #print(list_4)
#     list_6=[]
#     for i in list_4:
#         list_5=[]
#         for j in range(min(i),max(i)):
#             list_5=list_5+[j]
#         list_6=list_6+[list_5]
#     #print(list_6)
#     list_8=[]
#     for i in list_6:
#         list_7=[]
#         for j in i:
#             list_7=list_7+[list_1[j]]
#         list_8=list_8+[list_7]
#     #print(list_8)
#     list_9=[]
#     for i in list_8:
#         list_9=list_9+[i[::-1]]
#     #print(list_9)
#     list_10=[]
#     for i in list_9:
#         for j in i:
#             list_10=list_10+[j]
#     #print(list_10)
#     #for i in list_10:
#         #print(i,end=" ")
#     list_11=list_1[max(list_3):len(list_1)]
#     #print(list_11)
#     list_10=list_10+list_11[::-1]
#     #print(list_10)
#     for i in list_10:
#         print(i,end=" ")
# else:
#     print("Not enough numbers to reverse in a stream")


# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = int(input())

# if len(list_1) >= k:
#     list_3 = list(range(0, len(list_1), k))
#     list_10 = [list_1[i:j][::-1] for i, j in zip(list_3, list_3[1:])]
#     list_11 = list_1[list_3[-1]:]
#     list_10.extend([list_11[::-1]])
#     list_10 = [item for sublist in list_10 for item in sublist]

#     for i in list_10:
#         print(i, end=" ")
# else:
#     print("Not enough numbers to reverse in a stream")

# str  = "the moon bcjkd "

# def leng(str):
#     l = str.split()
#     return len(l[-1])

# print(leng(str))

# # class Solution:
# str = "race a car"
# def isPalindrome(str):
#     str = [char.lower() for char in str if char.isalnum()]
#     return str == str[::-1]

# print(isPalindrome(str))

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = int(input())
# new = [i**2 for i in list_1]
# print(new)


