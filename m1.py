# def transformSentence(sentence):
#     res = ""
#     for j in sentence[1:]:
#         if (ord(j)>ord(j-1)):
#             res = res + j.upper()
#         elif (ord(j)<ord(j-1)):
#             res = res + j.lower() 
#         elif ord(j)==ord(j-1):
#             res = res + j        
#     return res

# sentence = "a Blue MOON"
# transformSentence(sentence)

# def transformSentence(sentence):
#     res = sentence[0]
#     for i, j in enumerate(sentence[1:], start=1):
#         if ord(j) > ord(sentence[i-1]):
#             res += j.upper()
#         elif ord(j) < ord(sentence[i-1]):
#             res += j.lower()
#         else:
#             res += j
#     return res

# sentence = "a Blue MOON"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)



# def transformSentence(sentence):
#     res = sentence[0]
#     for i, j in enumerate(sentence[1:], start=1):
#         if sentence[i-1].islower():
#             res += j.upper()
#         elif sentence[i-1].isupper():
#             res += j.lower()
#         else:
#             res += j
#     return res

# sentence = "ab cB GG"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)

# def transformSentence(sentence):
#     res = sentence[0]
#     for i, j in enumerate(sentence[1:], start=1):
#         if ord(sentence[i]) < ord(sentence[j+1]):
#             res += i.upper()
#         elif ord(sentence[i]) > ord(sentence[j+1]):
#             res += sentence[j].lower()
#         else:
#             res += sentence[j]
#     return res

# sentence = "a Blue MOON"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)

# def transformSentence(sentence):
#     res = sentence[0]
#     for i, j in enumerate(sentence[1:], start=1):
#         if ord(sentence[i]) < ord(sentence[j+1]):
#             res += str(i).upper()
#         elif ord(sentence[i]) > ord(sentence[j+1]):
#             res += sentence[j].lower()
#         else:
#             res += sentence[j]
#     return res

# sentence = "a Blue MOON"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)

# def transformSentence(sentence):
#     res = sentence[0]
#     for i, j in enumerate(sentence[1:], start=1):
#         if ord(sentence[i]) < ord(sentence[j+1]):
#             res += sentence[str(i)].upper()
#         elif ord(sentence[i]) > ord(sentence[j+1]):
#             res += sentence[str(j)].lower()
#         else:
#             res += sentence[str(j)]
#     return res

# sentence = "a Blue MOON"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)

# def transformSentence(sentence):
#     res = sentence[0]
#     for i in sentence:
#         if ord(i) < ord(i+1):
#             res += i.upper()
#         elif ord(i) > ord(i+1):
#             res += i.lower()
#         else:
#             res += i
#     return res

# sentence = "a Blue MOON"
# transformed_sentence = transformSentence(sentence)
# print(transformed_sentence)



# def reverse_words_order_and_swap_cases(sentence):
#     srt = sentence.split(" ")
#     ans  = [i for i in srt[::-1]]
#     # print(ans)
#     res = ""
#     for i in ans:
#         for j in i:
#             if j.islower():
#                 j = j.upper()
#                 res = res + j
#             elif j.isupper():
#                 j = j.lower()
#                 res = res + j
#             # elif j == " ":
#             #     res = res + " " 
#         res = res + " "
#     return res
        # print(i,end=" ")# top = 0
        # bottom = n-1
        # left = 0
        # right = m-1
        
        # for i in range(left,right+1):
        #     print(matrix[left][i],sep=" ")
        # top += 1
        # while(top<=bottom):
        #     for i in range(top,bottom+1):
        #         print(matrix[i][right],sep=" ")
        # right -= 1
        
        # for i in range(right,left+1):
        #     print(amtrix[bottom][i],sep=" ")
        # bottom += 1
        # while(left<=right):
        #     for i in range(bottom,top):
        #         print(matirx[i][left],sep=" ")
    # res = ""
    # for i in ans:
    #     for j in i:
    #         if j.islower():
    #             res + j.upper()
    
    # return res



# sentence="rUns dOg"
# anss = reverse_words_order_and_swap_cases(sentence)
# print(anss)

# s = "Let's take LeetCode contest"
# ans = ""
# res = s.split(" ")
# for i in res:
#         ans += i[::-1]
#         ans += " "
# print(ans)



# top = 0
        # bottom = n-1
        # left = 0
        # right = m-1
        
        # for i in range(left,right+1):
        #     print(matrix[left][i],sep=" ")
        # top += 1
        # while(top<=bottom):
        #     for i in range(top,bottom+1):
        #         print(matrix[i][right],sep=" ")
        # right -= 1
        
        # for i in range(right,left+1):
        #     print(amtrix[bottom][i],sep=" ")
        # bottom += 1
        # while(left<=right):
        #     for i in range(bottom,top):
        #         print(matirx[i][left],sep=" ")


    # top = 0
    # bottom = n-1
    # left = 0
    # right = m-1
    # res = []
    # for i in range(left,right+1):
    #     res.append(matrix[left][i])
    # top += 1
    # while(top<=bottom):
    #     for i in range(top,bottom+1):
    #         res.append(matrix[i][right])
    # right -= 1
    
    # for i in range(right,left+1):
    #     res.append(matrix[bottom][i])
    # bottom += 1
    # while(left<=right):
    #     for i in range(bottom,top):
    #         res.append(matirx[i][left])
    # top += 1
    # if (top==bottom):
    #     return res








# list = [1,2,3,4,5]
# a = int(input())
# # B = 4//a
# try:
#     for i in list:
#         print(i)
#     print(a//0)
# # except Exception as e:
# #     print("Error",e)
# except ValueError as e:
#     print("fsvef",e)
# except ZeroDivisionError as e:
#     print("dbfdb",e)
# finally:
#     print("Code Completed")

# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(n-i+1):
#         print(i,end="")
#     for j in range(i-1):
#         print(" ",end=" ")
#     for j in range(1):
#         print(i,end=" ")
#     print()

# num = int(input())
# pow =  int(input())

# for i in range(1,pow+1):
#     res = num**i
# print(res)

# n  = int(input())

# sum = (n*(n+1))//2

# print(sum)

# text = "the man is laughing"
# new = text.split()
# res = [i[::-1] for i in new[::-1]]
# res1 = [i for i in new[::-1]]
# print(res) 
# print(res1)

# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact* i
# print(fact)

# n = int(input())
# def fun(n):
#     if n==1: return "Not Prime"
#     if n==2: return "Prime"

#     for i in range(2,n):
#         if n%i==0:
#             return "Not Prime"

#     return "Prime"

# print(fun(n))


# n = int(input())
# a = 0
# b = 1
# if n==1: c = a
# for i in range(n-1):
#         c = a + b
#         b = a
#         a = c

# print(c)

# n = int(input())
# l = n
# def func(n):
#     count = 0
#     sum = 0
#     while n>0:
#         last = n%10
#         n =n//10
#         count += 1
#         sum += last
#     return ("sum of digits:",sum,"No of digits:",count)

# print(func(n))


# n = int(input())
# rev = 0
# while(n>0):
#     last = n % 10
#     rev = rev*10 + last
#     n = n//10

# print(rev)

# n = int(input())
# res = 0
# power = 1
# while(n>0):
#     last = n % 10
#     res = res + last*power
#     power *= 2
#     n = n // 10

# print(res)

# n = int(input())

# ans = 0
# power = 1

# while(n>0):
#     last = n % 2
#     ans += last*power
#     power *= 10
#     n = n // 10P

# print(ans)

# A,B = map(int,input().split())
# if (A%2 ==0 and B%2 ==0):
#     print("He")
# elif(A%2 !=0 and B%2 !=0):
#     print("She")
# else:
#     print("Punished")

# list_1 = (1,2,3,45,2,6,3,"bjek")

# new = list_1.copy()
# print(new)
# list_1.append("vf")
# list_1.insert(2,345)
# list_1.extend([1,3,"ved"])
# list_1.remove("ved")
# list_1.pop()
# print(list_1)

# print(list_1.index(45))
# del list_1
# # print(list_1)

# srt ="bbngd3kj"
# print(len(srt))
# print(srt.capitalize())
# print(srt.center(10,"@"))
# print(srt.find("g"))
# print(srt.index("g"))
# print(srt.count("b"))
# print(srt.startswith("b",0,len(srt)))
# print(srt.endswith("k",0,len(srt)))
# print(srt.isalnum())
# print(srt.isalpha())
# print(srt.isdigit())
# print(srt.isupper())
# print(srt.islower())
# print(srt.lower())
# print(srt.upper())
# print(srt.split("g"))
# print(srt.strip())
# print(srt.rindex("3"))
# print(srt.replace("3","2"))


# dic = {"vdf":"vfs","ve":"vr"}

# print(dic.values())
# print(dic.keys())
# print(dic.items())
# print(dic.get("vdf"))
# print(dic.pop("ve"))
# # print(dic.popitem())
# print(dic)
# print(dic.clear())
# ans =  dic.copy()
# print(ans)
# ans.update({"cssv":"bngfbfg"})
# print(ans)

# list_1 = (1,2,3,4,5)
# y  = 0
# # list_2 = ("vev","gf","ert","frg","egt")

# res = dict.fromkeys(list_1,y)
# print(res)


# lst = {1,2,3,4,5}

# lst2 = {"vef",34,34.67,657}

# print(lst|lst2)
# print(lst&lst2)
# lst.pop()
# # lst.remove(2)
# print(lst)
# # lst.discard(34)
# # print(lst)

# n = int(input("Enter any odd number:"))

# for i in range(n):
#     for j in range(n):
#         if i == n//2 or j == n//2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# a , b = map(str,input().split())

# # import roman

# # a = int(input())

# # res = roman.ToRoman(a)

# # print(res)

# res1 = sorted(a)
# res2 = sorted(b)
# # print(res2)
# flag = 0
# for i in range(len(a)):
#     if res1[i] == res2[i]:
#         flag = 1
#     else:
#         flag = 0

# if flag :
#     print("True")
# else:
#     print("false")

# a = str(input())

# lst = list(map(str,input().split()))

# lst1  = [sorted(i) for i in lst]

# new = sorted(a)
# new_list = []
# count = 0
# for i in lst1:
#     if i == new:
#         count += 1
#         new_list.append(i)
#     else:
#         continue

# print(new_list)
# print(count)

# n = int(input("enter rows:"))
# m = int(input("enter columns"))

# for i in range(n):
#     for j in range(m):
#         print("*",end="")
#     print()

# n = int(input())
# char = ord("A")
# k = 0
# for i in range(1,2*n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print(chr(char + k),end="")
#         k += 1
#     k = 0
#     for j in range(i-n):
#         print(" ",end="")
#     for j in range(2*i-n):
#         print(chr(char+k),end="")
#         k +=1
#     k = 0
#     print()


# from collections import Counter
# def duplicates(arr, n): 
#             a = Counter(arr)
#             # print(a)
#             L = []
#             for i in a.keys():
#                 if a.get(i) > 1:
#                     L.append(i)
#             return sorted(L) if len(L) > 0 else [-1]

# arr = [2,3,1,2,3]
# n = 5
# print(duplicates(arr,n))


# def minimumSeconds(self, nums: List[int]) -> int:
#         dic = {}

#         for i in range(len(nums)):
#             if nums[i] not in dic:
#                 dic[nums[i]] = 1
#             else:
#                 dic[nums[i]] += 1

#         else:
#             return len(dic.keys()) - 1


# from collections import Counter

# # class Solution:
# def minimumSeconds(self, nums: List[int]) -> int:
#     # Count the frequency of each element in nums
#     counts = Counter(nums)
                    
#     # Check if all elements have a frequency of 1
#     if all(val == 1 for val in counts.values()):
#         return 1
#     else:
#     # Find the maximum frequency
#         max_freq = max(counts.values())
#     # Calculate the number of seconds required as 2 * (max_freq - 1) + 1
#         return 2 * (max_freq - 1) + 1



# n = int(input())
# k = 0
# m = 0
# char = 65
# for i in range(1,2*n):
#     if i > 0 and i <= n:
#         for j in range(n-i):
#             print(" ",end="")
#         k = 0
#         for j in range(2*i-1):
#             print(chr(char+k),end="")
#             k += 1
#     if i > n and i <= 2*n:
#         for j in range(i-n):
#             print(" ",end="")
#         k = 0
#         for j in range(2*i-n-2*m):
#             print(chr(char+k),end="")
#             k += 1
#         m += 2
#     print()

# n = int(input())
# char = 65
# k = 0
# for i in range(1,n+1) :
#     k = 0
#     for j in range(i):
#         print(chr(char+k),end="")
#         k +=1
#     print()

    

# def boundaryTraversal(mat, n, m):
#     ans = []

#     j = 0
#     for j in range(m):
#         ans.append(mat[0][j])
#     j -= 1

#     i = 0
#     for i in range(1, n):
#         ans.append(mat[i][j])
#     i -= 1
#     j -= 1

#     if n > 1:
#         while j >= 0:
#             ans.append(mat[i][j])
#             j -= 1
#         j += 1
#         i -= 1

#     if m > 1:
#         while i > 0:
#             ans.append(mat[i][j])
#             i -= 1

#     return ans

# digits = [9]
# res = ""
# for i in digits:
#     res = res + str(i)

# res = int(res) 
# res += 1
# ans = str(res)
# asn = []
# for i in ans:
#     asn.append(int(i))
# print(asn)

# def fun(n):
#         new = int(n)
#         res = 0
#         power = 1
#         ans = new
#         while(new > 0):
#             last = new % 10
#             last *= power
#             res += last
#             power *= 2
#             new = new // 10

#         return res
    
# a = str(input())
# b = str(input())
# res1 = fun(a)
# res2 = fun(b)

# # print(res1)
# # print(res2)

# fin = res1 + res2

# def func(fin):
#     n = fin
#     power = 1
#     ans = 0
#     while (fin>0):
#         last = fin % 2
#         last *= power
#         ans += last
#         power *= 10
#         fin = (fin // 2)

#     return str(ans)

# final = func(fin)

# print(final)


# def fun(n):
#     new = int(n)
#     res = 0
#     power = 1
#     ans = new
#     while(new>0):
#         last = new%10
#         last *= power
#         res += last
#         power *= 2
#         new = new // 10

#     return res
            
# a = str(input())
# b = str(input())
# res1 = fun(a)
# res2 = fun(b)

# # print(res1)
# # print(res2)

# fin = res1 + res2


# def func(fin):
#     n = fin
#     power = 1
#     ans = 0
#     while (fin>0):
#         last = fin % 2
#         last *= power
#         ans += last
#         power *= 10
#         fin = (fin // 2)

#     return str(ans)

# final = func(fin)
# print(final)
# return final



# n = 28
# res = ""
# while(n>0):
#     rem = n%26
#     n = n//26
#     res += "A"*n + chr(64+rem)

# print(res)

# print("A"*5)
# print(chr(65+3))

# nums = [1,2,3,1,1,3]
# count = 0
# i = 0
# # for i in range(len(nums)):
# j = i + 1
# while (j < len(nums) and i < j):
#     # j = i + 1
#     if (nums[i]==nums[j]):
#         count += 1
#     # j += 1
#     if (j==len(nums)-1):
#         i += 1
#         j = i + 1
#     j += 1
# print(count)

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# sum = 0
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if (i==j) or (i+j)==len(mat)-1:
#             sum += mat[i][j]
# print(sum)

# anss = 101
# final = anss^1
# print(final)