# # # Rahul has promised to take his little kids Akash and Anusha to the renownedshow.
# # #  Unfortunately Rahul got a bit late to return from work, but he did not want to disappoint the kids.
# # #  So he started off with them to the show in his car. 
# # # He thought to take a short route to reach the show on time but he was not sure if it is possible to reach the magic show venue at the point (x2, V2) from his house which is at a point (x1, Y₁)-

# # # Given coordinates of a source point (x1,y1), write a recursive function to determine if it is possible to reach the destination point (x2, y2).

# # # Note: From any point (x, y) there only two types of valid movements: (x, x + y) and (x + y, y).
# # # Sample Input 1:
# # # 12
# # # 10
# # # 26
# # # 12

# # # Sample Output 1:
# # # 

# # # Sample Input 2:
# # # 10
# # # 10
# # # 12
# # # 12

# # # Sample Output 2:
# # # False


# def fun(x1,y1,x2,y2):
#     if(x1>x2 or y1>y2):   #Base case
#         return False
#     elif(x1==x2 or y1==y2):   #Base case
#         return True
#     else:
#         return fun(x1+y1,y1,x2,y2) or fun(x1,x1+y1,x2,y2)
    

# x1,y1=5,10
# x2,y2=45,10    
# print(fun(x1,y1,x2,y2))



def small(a,b):
    if a>b:
        return b
    else:
        return a

sum=lambda x,y:x+y
diff=lambda x,y:x-y

print("Smaller is:",small((sum(-2,4)),diff(-2,-6)))