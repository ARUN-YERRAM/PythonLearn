# def twoSum(nums, target):
#     map = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in map:
#             return [map[complement], i]
#         map[nums[i]] = i
#     raise ValueError("No two sum solution")


# twoSum(10,20)


# n = max(list)

# print(n)

# def max(list):
#     max = -1
#     index = -1
#     for i in range(len(list)):
#         if list[i] > max:
#             max = list[i]
#             index = i
#     return index

# list = [1,3,5,2,4,6,4]
# # print(max,'index =',index,sep='\n')

# # ans  = max(list)

# # print(ans)

# list.sort()

# print(list[-2])

# print second largest element in list

# def second_max(list):
#     max = -1
#     sec_amx = -1

#     for num in list:
#         if num > max:
#             sec_max = max
#             max = num
        
#         elif num >sec_max and num!=max:
#             sec_max = num
    
#     return sec_max

# list = [1,3,5,2,4,6,4]
# ans = second_max(list)
# print(ans)

# def minimumSeconds(nums):
#         dic = {}

#         for i in range(len(nums)):
#             if nums[i] not in dic:
#                 dic[nums[i]] = 1
#             else:
#                 dic[nums[i]] += 1
        
#         return len(dic.keys() ) -1

# nums = [2,1,3,3,2]

# print(minimumSeconds(nums))

# def containsDuplicate(nums):
#         dic = {}
#         for i in range(len(nums)):
#             if nums[i] not in dic:
#                 dic[nums[i]] = 1
#             else:
#                 dic[nums[i]] += 1

#                 if dic[nums[i]] > 1:
#                     return True
#                     break

#         return False

# nums = [1,2,3,4] 
# print(containsDuplicate(nums))


# def containsNearbyDuplicate(nums , k):
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if  i!=j and nums[i]==nums[j] :
#                     if abs(i - j)<=k:
#                         return True

#         return False

# nums = [1,0,1,1]
# k = 1P

# print(containsNearbyDuplicate(nums, k))


st = 65
ts = "B"
print(chr(st))
print(ord(ts))

