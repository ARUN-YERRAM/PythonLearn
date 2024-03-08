# # import numpy as np
# # arr = np.array(range([100 for i in range(0,10) for i in range(0,4)]))
# # print(arr)

# # write a code for palindromic sequence
# def spring(n):
#     "fvdxbdxbdgb"
#     return n**2

# x =int(input())
# n=spring(x)
# print(n)


def is_palindromic(sequence):
    """
    Check if a given sequence is palindromic.

    Args:
        sequence (str or list): The sequence to be checked.

    Returns:
        bool: True if the sequence is palindromic, False otherwise.
    """
    # Convert the sequence to a string if it is a list
    if isinstance(sequence, list):
        sequence = ''.join(sequence)

    # Check if the sequence is equal to its reverse
    return sequence == sequence[::-1]

print(is_palindromic("saas"))

