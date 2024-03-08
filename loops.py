# def greater(a,b):
#     if(a>b):
#         print(a,"is greater")
#     else:
#         print(b,"is greater")    

# def lesser(a,b):
#     if(a<b):
#         print(a,"is lesser")
#     else:
#         print(b,"is lesser")    

# a=int(input("Enter number a:"))
# b=int(input("Enter number b:"))
# greater(a,b)
# lesser(a,b)

# str=input()

# print(str[::-1])

# string_list = input("Enter a string: ").split()

# reversed_strings = [string[::-1] for string in reversed(string_list)]

# output = ' '.join(reversed_strings)
# print(output)

# l=["I","You"]
# v=["Play","Love"]
# o=["Hockey","Football"]
# for j in range(2):
#     for k in range(2):
#         for m in range(2):
#                 print(l[j ]+v[k ]+o[m ])
            

# i=0
# num=int(input("Enter an integer:"))

# x=num//4
# k=x-i
# c=x-i+1
# z=x-i+2
# f=x-i-1
# if(k+c+z+f==num):
#     print(num,"is Consecutive Four Sum Number")
# else:
#     print(num,"is not Consecutive Four Sum Number")

# str=input()
# print(str[::-1])

# input_string = input("Enter a string: ")

# reversed_string = ' '.join(word[::-1] for word in input_string.split()[::-1])

# print(reversed_string)

# from functools import reduce

# def sum_of_digits(num):
#     return reduce(lambda x, y: int(x) + int(y), str(num))

# # Test case 1
# list_elements = input("Enter list elements: ").split()
# resultant_list = [sum_of_digits(num) for num in list_elements]
# print("Resultant List:", resultant_list)

# # Test case 2
# list_elements = input("Enter list elements: ").split()
# resultant_list = [sum_of_digits(num) for num in list_elements]
# print("Resultant List:", resultant_list)


# istr = input("Enter a string: ")
# st = istr.split()

# rs = [word[::-1] for word in st[::-1]]
# rt = ' '.join(rs)

# print(rt)

l = list(map(int, input("Enter list elements: ").split()))
x = int(input("Enter search key: "))

count = l.count(x)
if count > 0:
    print(x, "exists, count of", x, "is", count)
else:
    print(x, "does not exist")

largest = max(l)
smallest = min(l)

print("Largest element:", largest)
print("Smallest element:", smallest)

