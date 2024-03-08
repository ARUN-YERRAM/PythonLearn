# # Arun is working in an office which is N blocks away from his house. He wants to minimize the time it 
# takes him to go from his house to the office. He can either take the office cab or he can walk to the 
# office. Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but 
# whenever he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes 
# back to the office. 
# The cab crosses a total distance of N meters when going from office to Arun's house and vice versa, 
# whereas Arun covers a distance of (√2)*N while walking. Write a program to help Arun to find 
# whether he should walk or take a cab to minimize the time.

# import math 

# N=int(input("Enter no of blocks:"))
# v1=int(input("Enter walk velocity:"))
# v2=int(input("Enter velocity:"))

# t1=math.sqrt(2)*N//v1
# t2=N//v2

# if(t1>t2):
#     print("Cab is Better")
# else:
#     print("Walk is Better")    

# import json
# for i in range(5):
#     with open("p2.py","a") as f:
#         d=f.write("Code appended")
#         print(d)
#         print(f.tell())

import os
os.rename("p3.py","prctse.py")