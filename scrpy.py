# def fun(matrix):
#         top = 0
#         bottom = len(matrix)-1
#         left = 0
#         right = len(matrix)-1

#         res = []

#         while(top<=bottom and left<=right):
#             for i in range(left,right+1):
#                     res.append(matrix[top][i])
#             top = top + 1

#             for i in range(top,bottom+1):
#                 res.append(matrix[i][right])
#             right = right - 1

#             if(top<=bottom):
#                 for i in range(right,left-1,-1):
#                     res.append(matrix[bottom][i])
#                 bottom = bottom-1
#             if(left<=right):
#                 for i in range(bottom,top-1,-1):
#                     res.append(matrix[i][left])
#                 left = left + 1
#         return res


# arr = [[1,2,3],[4,5,6],[7,8,9]]

# res = fun(arr)

# print("The spiral matrix is:",res)


import numpy

