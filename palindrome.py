# dic = {"apple":12,"banana":123,"guava":1234}
# # print(dic)
# # for i in dic.values():
# #     print(i)
# # dic["jelly"]=12345
# # print(dic)

# # print(dic["apple"])

# dic1={"12":12,"11":11,"13":13}
# dic.update(dic1)
# print(dic)

# list1=(1,2,3,4)
# list2=("apple", "banana", "guava")
# print(dict(zip(list1,list2)))
# print(dic.pop("banana"))
# print(dic)

# print(dic.items())

# str = input()
# dic = {}
# count = 0
# for i in str:
    
#     if i not in dic:
#         dic[i]=count+1
#     else:
#         dic[i]=dic[i]+1

# print(dic)

# list = [i for i in range(10)]
# print(list)

# list.append(1224)
# print(list)
# print(list.index(9))

# l = [int(x) for x in input().split()]
# l.sort()
# print(l)

# list=["hello",[1,2,3],34,23.45,True]
# # print(l[:3])
# list.append(12)
# print(list)
# ls=list.copy()
# print(ls)
# list.insert(1,1234)
# list.extend([1,2,3,4])
# print(list)
# list.pop()
# list.remove(1234)
# list.clear()
# print(list)

# list = ["hello","Morning"]
# l=set()
# for i in list:
#     for j in i:
#         l.add(j)
# print(l)

# list=[1,2,4,6,7,9,10]
# ls=[]
# for i in range(max(list)+1):
#     if i in list:
#         ls.append(i)
#     else:
#         ls.append(-1)
# print(ls)

# ls1=[1,3,5,7,9]
# ls2=ls1[::-1]
# ls3=[]
# for i in range(len(ls2)):
#     ls3.append(ls1[i]+ls2[i])
# print(ls3)

# ls=[1,2,3,4,5]
# ls1=[1,3,4,5,3]
# res=map(lambda x,y:x+y,ls,ls1)
# print(list(res))

# val=[[1,2,3],[5,4,3],[6,8,7]]
# res=[y for x in val for y in x]
# print(set(res))

# print("\a")


# r=int(input("Enter row size:"))
# c=int(input("Enter column size:"))
# m=[]
# sum=0
# for i in range(r):
#     row=[]
#     for j in range(c):
#         row.extend([5*i for i in range(1,6)])
#     m.append(row)

# for i in range(r):
#     for j in range(c):
#         print("%2d"%m[i][j],end=" ")
#     print()
# import numpy as np
# mat=np.array()

# def fun(arr1,arr2):
#     arr3 =[]
#     for i in range(len(arr1)):
#         row=[]
#         for j in range(len(arr2)):
#             row.append(arr1[i]*arr2[j])
#         arr3.append(row)
        
#         return arr3


# arr1= list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# res=fun(arr1,arr2)
# print(res)

# str = "the KIND HEART ALWAYS FACES SEVERE PAIN"
# print(str.replace("PAIN","GAIN"))
# print(str.startswith("KIND"))

# str=input().split()
# print(str)
# str=""
# str=str+"svfz"
# print(str)

# # srt=[i[::-1] for j in str[::-1] for i in j]
# # print(srt)
# print(str)







# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# strs = ["flower","flow","flight"]
# l=[min(len(i) for i in strs)]
# print(l)
# res=""
# for i in strs:
#     for j in i:
#         for k in range(l[0]):

# print(res)


# def longest_common_prefix(strs):
#     if not strs:
#         return ""

#     # Find the shortest string in the array
#     min_len = min(len(s) for s in strs)
    
#     # Initialize the common prefix
#     common_prefix = ""
    
#     # Iterate over characters in the shortest string
#     for i in range(min_len):
#         char = strs[0][i]  # Get the character at position i from the first string
        
#         # Check if the character is the same in all strings
#         if all(s[i] == char for s in strs):
#             common_prefix += char
#         else:
#             break
    
#     return common_prefix

# # Example usage
# strs1 = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs1))  # Output: "fl"

# strs2 = ["dog", "racecar", "car"]
# print(longest_common_prefix(strs2))  # Output: ""



# class Solution:
# def longestCommonPrefix(strs):

#         if not strs:
#             return ""

#         mini=min(len(s) for s in strs)

#         res=""

#         for i in range(mini):
#             char=strs[0][i]

#             if all(s[i]==char for s in strs):
#                 res+=char
#             else:
#                 break
        
#         return res
    
# str=["dog", "racecar", "car"]
# rs=longestCommonPrefix(str)
# print(rs)

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def fun(nums,val):
    rss=[]
    for i in range(len(nums)):
            if nums[i]!=val:
                rss.append(nums[i])
                
    return (len(rss),'nums =',rss)


nums = [3,2,2,3]
val = 3
res=fun(nums,val)
print(res)

