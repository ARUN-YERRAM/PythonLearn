# from collections import OrderedDict

# def FirstNonRepeating(A):
#     char_freq = OrderedDict()  # This will store the character frequencies in order of their appearance
#     result = []  # This will store the result as we process the input stream

#     for char in A:
#         # Increment the frequency of the current character
#         char_freq[char] = char_freq.get(char, 0) + 1

#         # Check for the first non-repeating character
#         found = False
#         for key, freq in char_freq.items():
#             if freq == 1:
#                 result.append(key)
#                 found = True
#                 break

#         # If no non-repeating character is found, append '#'
#         if not found:
#             result.append('#')

#     return "".join(result)

# n=input()
# c=input()
# # Test cases
# print(FirstNonRepeating(n))  # Output: "abb"
# print(FirstNonRepeating(c))


import numpy as np
A = np.array([[1,2,3,],[4,5,6]])
print(A.ndim)