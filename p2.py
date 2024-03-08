# from collections import OrderedDict

# def FirstNonRepeating(A):
#     freq = OrderedDict()
#     result = []

#     for char in A:
#         freq[char] = freq.get(char,0)+1
#         found = False
#         for key,value in freq.items():
#             if value == 1:
#                 result.append(key)
#                 found = True
#                 break
        
#         if not found:
#             result.append("#")
    
#     return "".join(result)

# n=input()
# c=input()
# # Test cases
# print(FirstNonRepeating(n))  # Output: "abb"
# print(FirstNonRepeating(c))



# def rec(nums, idx):
#     if idx >= len(nums):
#         return 0
#     return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))

# def findMaxSum(arr, N):
#     return rec(arr, 0)

# if __name__ == "__main__":
    
#     arr = [5, 5, 10, 100, 10, 5]
#     N = len(arr)

#     print(findMaxSum(arr, N))   
#     # Code appendedCode appendedCode appendedCode appendedCode appendedCode appendedCode appendedCode appendedCode appendedCode appended

# '''11. Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file
# sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make
# a visualization focusing on the data in this column. '''
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_csv("sitka_weather_2018_simple.csv")
# rainfall = data["PRCP"]
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
# fig.suptitle("Rainfall Data Visualization")
# axes[0, 0].boxplot(rainfall,vert=False)
# axes[0, 0].set_title("Boxplot")
# axes[0, 0].set_xlabel("Rainfall (inches)")
# axes[0, 1].hist(rainfall, bins=20, density=True, alpha=0.7)
# axes[0, 1].set_title("Histogram")
# axes[0, 1].set_xlabel("Rainfall (inches)")
# axes[0, 1].set_ylabel("Frequency")
# axes[1, 0].plot(data.index, rainfall)
# axes[1, 0].set_title("Line Graph")
# axes[1, 0].set_xlabel("Day")
# axes[1, 0].set_ylabel("Rainfall (inches)")
# axes[1, 1].scatter(data.index, rainfall, alpha=0.7)
# axes[1, 1].set_title("Scatter Plot")
# axes[1, 1].set_xlabel("Day")
# axes[1, 1].set_ylabel("Rainfall (inches)")
# plt.show()

# import numpy as np
# import random
# #indexed series
# index = [("bombay",2022),("bombay",2023),("bombay",2024),
#          ("shimla",2022),("shimla",2023),("shimla",2024),
#          ("jaipur",2022),("jaipur",2023),("jaipur",2024)]
# car_sales = [random.randint(230,500) for x in range(9)]
# j = pd.Series(data=car_sales,index=index)
# #print("Single Level", j)
# k = pd.MultiIndex.from_tuples(index,names=["city","year"]) #created a multiindex object allows me to access data level wise
# j = j.reindex(k)
# #print(j["shimla",2024])
# #print(j["jaipur"])
# #print(j[slice(None),2024])
# b = pd.DataFrame(data=car_sales,index=k)
# print(b.loc[(slice(None),2022),:]) 
