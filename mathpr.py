# # 1 Problem
# n=int(input(("Enter size of vector:")))

# v=[]

# print("enter elements of vector:")

# for i in range(n):
#     v.append(int(input()))
# print(v)    


# 2 problem

# r=int(input("Enter size of row:"))
# c=int(input("Enter size of column:"))
# m=[]
# print("Enter elements of vector:")
# for i in range(r):
#     row=[]
#     for j in range(c):
#         row.append(int(input()))
#     m.append(row)
# print("Column vector:")
# for i in range(r):
#     for j in range(c):
#         print(m[i][j],end=" ")
#     print()    


# 3 Problem

# r=int(input("Enter row size:"))
# c=int(input("Enter column size:"))
# m=[]
# if(r==c):
#     print("Enter elements of vector:")

#     for i in range(r):
#         row=[]
#         for j in range(c):
#             row.append(int(input()))
#         m.append(row)

#     print("Principal diagonal elements:")
#     for i in range(r):
#         for j in range(c):
#             if(i==j):
#                 print(m[i][j],end=" ")
#         print()        
# else:
#     print("It is not a square matrix")

# 4 Problem

# r=int(input("Enter row size:"))
# c=int(input('Enter column size:'))
# m=[]
# if(r==c):
#     print("Enter elements of Matrix:")

#     for i in range(r):
#         row=[]
#         for j in range(c):
#             row.append(int(input()))
#         m.append(row)

#     print("Square Matrix:")
#     for i in range(r):
#         for j in range(c):
#             print((m[i][j]),end=" ")
#         print()

# else:
#     print("It's not a Square Matrix")                    

# 5 Problem

# r=int(input("Enter row size:"))
# c=int(input("Enter column size:"))
# m=[]
# print("Enter elements of Matrix:")

# for i in range(r):
#     row=[]
#     for j in range(c):
#         row.append(int(input()))
#     m.append(row)

# print("Original Matrix:")
# for i in range(r):
#     for j in range(c):
#         print(m[i][j],end=" ")
#     print()

# print("Transposed Matrix:")
# for i in range(c):
#     for j in range(r):
#         print(m[j][i],end=" ")
#     print()

# 6 Problem

# Find sum of two vectors
# v1 = list(map(int,input("Enter first vector values: ").split()))
# v2 = list(map(int,input("Enter second vector values: ").split()))
# # print(v1,v2)
# v3 =[]
# print("Vector 1: ",v1)
# print("Vector 2: ",v2)
# if len(v1)==len(v2):
#     for i in range(len(v1)):
#         v3.append(v1[i]+v2[i])
#     print("Resultant vector: ",v3)
# else:
#     print("Vector addition not possible")


#7 Find difference of two vectors


# v1 = list(map(int,input("Enter first vector values: ").split()))
# v2 = list(map(int,input("Enter second vector values: ").split()))
# v3 =[]
# print("Vector 1: ",v1)
# print("Vector 2: ",v2)
# if len(v1)==len(v2):
#     for i in range(len(v1)):
#         v3.append(v1[i]-v2[i])
#     print("Resultant vector: ",v3)
# else:
#     print("vector diff not poss")


# 8 To display higher order matrix

# r = int(input("Enter row size: "))
# c = int(input("Enter column size: "))
# m = []
# print("Enter the matrix\n")
# for i in range(r):
#     row = []
#     for j in range(c):
#         row.append(int(input()))
#     m.append(row)
# print("Higher order Matrix:\n")
# for i in range(r):
#     for j in range(c):
#         print("%2d"%m[i][j],end=" ")
#     print()


# 9 To find Sum of matrix

# r1 = int(input("Enter row size: "))
# c1 = int(input("Enter column size: "))
# m1 = []
# print("Enter matrix 1 values: ")
# for i in range(r1):
#     row = []
#     for j in range(c1):
#         row.append(int(input()))
#     m1.append(row)
# print("Matrix 1:")
# for i in range(r1):
#     for j in range(c1):
#         print("%2d"%(m1[i][j]),end=" ")
#     print()
# r2 = int(input("Enter row size: "))
# c2 = int(input("Enter column size: "))
# m2 = []
# print("Enter matrix 2 values: ")
# for i in range(r2):
#     row = []
#     for j in range(c2):
#         row.append(int(input()))
#     m2.append(row)
# print("Matrix 2:")
# for i in range(r2):
#     for j in range(c2):
#         print("%2d"%(m2[i][j]),end=" ")
#     print()
# if(r1==r2 and c1==c2):
#     m3=[]
#     for i in range(r1):
#         row=[]
#         for j in range(c1):
#             row.append(m1[i][j]+m2[i][j])
#         m3.append(row)
#     print("Sum of Matrices:")
#     for i in range(r1):
#         for j in range(c1):
#             print("%2d"%(m3[i][j]),end=" ")
#         print()
# else:
#     print("Addition not possible")


#  10 Multiplication of matrix

# r1 = int(input("Enter row size: "))
# c1 = int(input("Enter column size: "))
# m1 = []
# print("Enter matrix 1 values: ")
# for i in range(r1):
#     row = []
#     for j in range(c1):
#         row.append(int(input()))
#     m1.append(row)
# print("Matrix 1:")
# for i in range(r1):
#     for j in range(c1):
#         print("%2d"%(m1[i][j]),end=" ")
#     print()
# r2 = int(input("Enter row size: "))
# c2 = int(input("Enter column size: "))
# m2 = []
# print("Enter matrix 2 values: ")
# for i in range(r2):
#     row = []
#     for j in range(c2):
#         row.append(int(input()))
#     m2.append(row)
# print("Matrix 2:")
# for i in range(r2):
#     for j in range(c2):
#         print("%2d"%(m2[i][j]),end=" ")
#     print()
# m3=[]
# if(c1==r2):
#     print("Multiplication of two matrices")
#     for i in range(r1):
#         row=[]
#         for j in range(c2):
#             sum=0
#             for k in range(r2):
#                 sum = sum+(m1[i][k]*m2[k][j])
#             row.append(sum)
#         m3.append(row)
#     for i in range(r1):
#         for j in range(c2):
#             print("%2d"%(m3[i][j]),end=" ")
#         print()
# else:
#     print("Matrix Multiplication not possible")



#  11 TRACE OF A MATRIX
# Using user input
# r=int(input("Enter row size:"))
# c=int(input("ENter col size:"))
# m=[]
# for i in range(r):
#     row=[]
#     for j in range(c):
#         row.append(int(input()))
#     m.append(row)
# print("matrix:")
# for i in range(r):
#     for j in range(c):
#         print("%2d"%(m[i][j]),end=" ")
#     print()
# if(r==c):
#     trace=0

#     for i in range(r):
#         trace=trace+m[i][i]
#     print("Trace:",trace)
# else:
#     print("It is not a Square  Matrix")



# # Using Function

# from numpy import array,trace
# M=array([[1,2,3],[1,3,8],[1,2,4]])
# t=trace(M)
# print("Trace= ",t)



# 12 To find determinant of a Matrix

import numpy
from numpy import array
from numpy.linalg import det
A = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)

B = det(A)
print(B)


# 13 Inverse of a Matrix
#  Finding an inverse of a Given array

# import array
# arr=numpy.array([[2,8],[10,9]])
# print(arr)
# invrsearray=numpy.linalg.inv(arr)
# print("Inverse array is:",)
# print(invrsearray)

# 14 rank of a Matrix 2*2

# import numpy as np
# from numpy.linalg import matrix_rank
# mat1=np.array([[1,2],[3,7]])
# print("Mat1:",mat1)

# rank=matrix_rank(mat1)
# print("The Rank is:",end="")
# print(rank)



# 15 To find rank of a matrix 3x3

# import numpy as np
# from numpy.linalg import matrix_rank


# mat1=np.array([[1,2,3],[3,6,9],[2,4,6]])
# print("Mat1:",mat1)

# rank=matrix_rank(mat1)
# print("The Rank is:",end="")
# print(rank)

#  Using user input

# import numpy as np
# from numpy.linalg import matrix_rank
# r=int(input("Enter no of rows:"))
# c=int(input("Enter no of columns:"))
# m=[]

# print("Enter matrix values:")
# for i in range(r):
#     v=[]
#     for j in range(c):
#         v.append(int(input()))
#     m.append(v)
# print("Matrix:")
# for i in range(r):
#     for j in range(c):
#         print("%d"%m[i][j],end=" ")
#     print()
# r=matrix_rank(m)
# print("Rank of the matrix:",r)


# 4.3  To solve system of equations 3x+y = 9 , x + 2y = 8

# import numpy as np
# A=np.array([[3,1],[1,2]])
# B=np.array([9,8])
#sol = np.linalg.solve(A,B)
# print("Solution: ",sol)



# 4.4 Application Problem tp solve System of equations
# """ A lady bought 12 books and 6 bags for $102 on a specific day. The next day,she bought 10 books 10 bags for $110 .Assuming the price of 
# of bags didn't change in two days, what is the price of one book and bag?"
# 12a + 6b = 102 , 10a + 10b = 110   """

# import numpy as np
# A= np.array([[12,6],[10,10]])
# B=np.array([102,110])
# X=np.linalg.solve(A,B)

# print("The price of one book and bag is:",X)




# 2x+4y+z = 1 , x-2y-3z = 2, x+y-z = -1

# import numpy as np
# A=np.array([[2,4,1],[1,-2,-3],[1,1,-1]])
# B=np.array([1,2,-1])
# sol=np.linalg.solve(A,B) 
# print("Solution: ",sol)


# 5.1 eigen values and eigen vectors


# import numpy as np
# from numpy.linalg import eig
# a=np.array([[8,-8,2],[4,-3,-2],[3,-4,1]])
# w,v=eig(a)
# print("E-value:",w)
# print("E-vector",v)


# 5.2 Eigen values and Eigen Vectors


# import sympy as sp
# mat=sp.Matrix([[8,-8,-2],[4,-3,-2],[3,-4,1]])
# print(mat)
# eigen=mat.eigenvects()
# for i in range(3):
#     print("\nEigen value:",eigen[i][0])
#     print("\nNumber of times Eigen value is repeated:",eigen[i][1])
#     print("\nEigen vector:\n",eigen[i][2])



# # 6.1 verification of cayley hamiltonian theorem


# import numpy as np
# from scipy import linalg as la
# A = np.array([[5,-2],[1,2]])
# trace=np.trace(A)
# det=la.det(A)
# I=np.eye(2)
# print(A @ A - trace * A + det * I)


# 6.2 Cayley hamiltonian theorem for 3*3

# import numpy as np
# from numpy import linalg as la
# s=0
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# t=np.trace(a)
# d=la.det(a)
# i=np.eye(3)
# def getMatrixMinor(m,i,j):
#     return ([row[:j]+row[j+1:] for row in (m[:i]+m[i+1:])])

# for i in range(3):
#     s+=round(la.det(getMatrixMinor([[1,2,3],[4,5,6],[7,8,9]],i,i)))
# print(a@a@a-t*a@a+s*a-d*i)


# 7.1  To diagonalize the given matrix


# import sympy as sp
# m=sp.Matrix([[-4,-4,-8],[4,6,4],[6,4,10]])
# print("Matrix:\n",m)
# P,D=m.diagonalize()
# print("Modal Matrix:",P)
# print("diagonal matrix:",D)


# 7.2 Singular Value decomposition of a Matrix


# from numpy import array
# from scipy.linalg import svd
# A=array([[1,1,0],[0,1,1]])
# print(A)
# V,S,VT=svd(A)
# print(V)
# print(S)
# print(VT)


# # 8.1  Program of Partial Derivatives

# from sympy import *
# x,y = symbols("x,y")

# function = x**2 * y**3 + 12*y**4
# print("Partial derivative wrt x =",diff(function,x))
# print("Partial derivative wrt y =",diff(function,y))
# print("Second order partial derivaives wrt x   = ",diff(function,x,x))
# print("Second order partial derivaives wrt y  = ",diff(function,y,y))
# print("Second order partial derivaives wrt x and y = ",diff(function,x,y))
# print("Second order partial derivaives wrt y and x = ",diff(function,y,x))



# 8.2  Partial derivative of a function using user input

# from sympy import *
# x,y = symbols("x,y")
# print("Enter the function")
# u = input()

# print("Partial Derivative wrt x =",diff(u,x))
# print("Partial Derivative wrt y =",diff(u,y))
# print("Second order partial Derivative wrt x =",diff(u,x,x))
# print("Second order partial Derivative wrt y =",diff(u,y,y))
# print("Second order partial Derivative wrt x and y =",diff(u,x,y))
# print("Second order partial Derivative wrt y and x =",diff(u,y,x))



# # 9.1  Jocobian for two variables

# from sympy import *
# x ,y = symbols("x , y")
# print("Give the functions u,v in 2 separate lines")
# u = input()
# v = input()

# a1,a2 = diff(u , x),diff(u,y)
# b1,b2= diff(v,x),diff(v,y)
# result = Matrix([[a1,a2],[b1,b2]])
# print(result)
# print("The Jacobian of u,v with respect to x,y is",result.det())



# 9.2 Jocobian for three variables

# from sympy import *
# x ,y, z = symbols("x , y , z")
# print("Give the functions u,v,w in 3 separate lines")
# u = input()
# v = input()
# w = input()

# a1,a2,a3 = diff(u,x),diff(u,y),diff(u,z)
# b1,b2,b3 = diff(v,x),diff(v,y),diff(v,z)
# c1,c2,c3 = diff(w,x),diff(w,y),diff(w,z)
# result = Matrix([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])
# print(result)
# print("The Jacobian of u,v,w with respect to x,y,z is",result.det())



# 9.3 To check functional dependency of given function

# from sympy import *
# print("number of functions:")
# num = int(input())
# if num == 2:
#     x , y = symbols("x,y")
#     print("give functions u,v in 2 separate lines")
#     u= input()
#     v=input()
#     a1,a2=diff(u,x),diff(u,y)
#     b1,b2=diff(v,x),diff(v,y)
#     result = Matrix([[a1,a2],[b1,b2]])
#     print(result)
#     print("The Jacobian of u,v with respect to x,y is",result.det())
# elif num == 3:
#     x,y,z=symbols("x,y,z")
#     print("Give the functions u,v, w in 3 separate lines")
#     u=input()
#     v=input()
#     w=input()
#     a1,a2,a3=diff(u,x),diff(u,v),diff(u,z)
#     b1,b2,b3=diff(v,x),diff(v,y),diff(v,z)
#     c1,c2,c3=diff(w,x),diff(w,y),diff(w,z)
#     result= Matrix([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])
#     print(result)
#     print("The Jacobian of u,v,w with respect to x,y,z is",result.det())

# if result.det()==0:
#     print("Functions are linearly independent")
# else:
#     print("Functions are linearly dependent")


# 10.1 # Gradient of a scalar function

# from  sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z")
# f =  x**2*y*z
# dx = diff(f,x)
# dy = diff(f,y)
# dz = diff(f,z)
# grad = np.array([dx,dy,dz])
# print("Gradient =",grad)


# 10.2 # Divergence of a vector function

# from sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z")
# variables = symbols("x,y,z")
# f1 = x**2
# f2 = y**3
# f3 = z*x

# F = np.array([f1,f2,f3])
# s = 0
# for i in range(3):
#     s=s+diff(F[i],variables[i])
# print("Divergence =",s)


# 10.3 # Curl of a vector function


# from sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z")
# f1 = x*y*z
# f2 = 3*x**2*y
# f3 = (x*z**2)-(y**2*z)
# point = {x:1, y:-1, z:1}
# a = diff(f3,y) - diff(f2,z)
# b = -diff(f3,x) + diff(f1,z)
# c = diff(f2,x) - diff(f1,y)

# curl = np.array([a.subs(point),b.subs(point),c.subs(point)])
# print("Curl =",curl)


# 10.1 # Gradient of a scalar function (user input)


# from  sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z")
# f =  input("Enter the function:")
# dx = diff(f,x)
# dy = diff(f,y)
# dz = diff(f,z)
# grad = np.array([dx,dy,dz])
# print("Gradient =",grad)


# 10.2 # Divergence of a vector function  (user input)


# from sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z") 
# variables = symbols("x,y,z")
# f1 = input("Enter f1:")
# f2 = input("Enter f2:")
# f3 = input("Enter f3:")

# F = np.array([f1,f2,f3])
# s = 0
# for i in range(3):
#     s=s+diff(F[i],variables[i])
# print("Divergence =",s)


# 10.3 # Curl of a vector function (user input)


# from sympy import *
# import numpy as np
# x,y,z = symbols("x,y,z")
# f1 = input("Enter f1:")
# f2 = input("Enter f2:")
# f3 = input("Enter f3:")

# point = {x:1, y:-1, z:1}
# a = diff(f3,y) - diff(f2,z)
# b = -diff(f3,x) + diff(f1,z)
# c = diff(f2,x) - diff(f1,y)

# curl = np.array([a.subs(point),b.subs(point),c.subs(point)])
# print("Curl =",curl)


# 11.1) Directional derivative

# from sympy import *
# import numpy as np
# def norm(vector):
#     s = 0
#     for v in vector:
#         s = s + v**2
#     return sqrt(s)
# x,y,z = symbols("x,y,z")
# f = x*y**2 + y*z**2
# vector = np.array([1,2,2])
# points = {x:2,y:-1,z:1}
# dx = diff(f,x)
# dy = diff(f,y)
# dz = diff(f,z)
# grad = np.array([dx.subs(points),dy.subs(points),dz.subs(points)])
# print("Gradient=",grad)
# nrm = norm(vector)
# print("Norm=",nrm)
# unit_vector=[]
# for v in vector:
#     unit_vector.append(v/nrm)
# print("Unit Vector =",unit_vector)
# print("Directional derivative =",np.dot(grad,unit_vector))


# 11.1) Directional derivative  (user input)

# from sympy import *
# import numpy as np
# def norm(vector):
#     s = 0
#     for v in vector:
#         s = s + v**2
#     return sqrt(s)
# x,y,z = symbols("x,y,z")
# f = input()
# vector = np.array([2,1,2])
# points = {x:1,y:1,z:1}
# dx = diff(f,x)
# dy = diff(f,y)
# dz = diff(f,z)
# grad = np.array([dx.subs(points),dy.subs(points),dz.subs(points)])
# print("Gradient=",grad)
# nrm = norm(vector)
# print("Norm=",nrm)
# unit_vector=[]
# for v in vector:
#     unit_vector.append(v/nrm)
# print("Unit Vector =",unit_vector)
# print("Directional derivative =",np.dot(grad,unit_vector))


# 12) Angle between two surfaces

# from sympy import *
# import numpy as np
# def gradient(f,points):
#     dx=diff(f,x)
#     dy=diff(f,y)
#     dz=diff(f,z)
#     grad=np.array([dx.subs(points),dy.subs(points),dz.subs(points)])
#     return grad
# def gradient_norm(grad):
#     s=0
#     for v in grad:
#         s=s+v**2
#     return sqrt(s)
# x,y,z = symbols("x,y,z")
# s1=x*2+y*2+z*2-9
# s2=x*2+y*2-z-2
# points={x:2,y:-1,z:2}
# grad1=gradient(s1,points)
# print("Gradient of 1st surface = ",grad1)
# grad2=gradient(s2,points)
# print("Gradient of 2nd surface = ",grad2)
# n1=gradient_norm(grad1)
# n2=gradient_norm(grad2)
# cosTheta=np.dot(grad1,grad2)/(n1*n2)
# print("Theta=",acos(cosTheta))

# 13)

#Evaluation of Double Integrals with constant and variable limists
# from sympy import *
# x,y=symbols("x,y")
# #constant limits
# print("Double integral with constant limits: ",integrate(x*y,(x,0,2),(y,0,2)))
# #variable limits
# print("Double integral with variable limits: ",integrate(x*y,(x,0,y),(y,0,1)))

# # 14)

# #Evaluation of Triple Integrals with constant and variable limists
# from sympy import *
# x,y,z=symbols("x,y,z")
#constant limits
# print("Double integral with constant limits: ",integrate(x*y*z,(x,0,1),(y,0,1),(z,0,1)))
# #variable limits
# print("Double integral with variable limits: ",integrate(exp(z),(z,0,x+y),(y,0,1-x),(x,0,1)))


# 15.1) Solving First Order Ordinary Differential Equations

# from sympy import *
# x = symbols("x")
# y = Function('y')
# dsolve(Derivative(y(x),x)+2*y(x))



# 15.2) Solving First Order Ordinary Differential Equations

# from sympy import *
# x = symbols("x")
# y = Function('y')
# dsolve(Derivative(y(x),x)+y(x)/(x*log(x))-2*x)


# 15.3) Solving First Order Ordinary Differential Equations

# from sympy import *
# x = symbols("x")
# y = Function('y')
# dsolve(Derivative(y(x),x)+y(x)*cos(x)-sin(x)*cos(x))


# 15.4) Solving First Order Ordinary Differential Equations.

# from sympy import *
# x = symbols("x")
# y = Function('y')
# dsolve(Derivative(y(x),x,x)+6*Derivative(y(x),x)+9*y(x))