# # n=int(input())

# # for i in range(n):
# #     for j in range(i):
# #         print("1",end="")
# #     for j in range(2*n-2*i-1):
# #         print("*",end="")
# #     for j in range(i):
# #         print("0",end="")
# #     print()            

# x,y,z=[int(i) for i in input().split()]
# print(x+y-z)


    #  '''Write a program to generate the following pattern.
    #  *********
    #  b******* b
    #  bb***** bb
    #  bbb***bbb
    #  bbbb*bbbb

    #  Input and Output Format:
    # Input consists of a single integer that corresponds to n, the number of rows. n is always an odd number.
    
    # Sample Input :
    # 5
    
    # Sample Output :
    # *********
    # b******* b
    # bb***** bb
    # bbb***bbb
    # bbbb*bbbb
    # '''
    
n=int(input())

for i in range(n):
    for j in range(i):
        print("b",end="")
    for j in range(2*n-2*i-1):
        print("*",end="")
    for j in range(i):
        print("b",end="") 
    print()           
