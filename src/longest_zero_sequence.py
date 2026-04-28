import numpy as np

def longest_zero_sequence_rolled(arr1):
    """
    Finds the longest sequence of zeros in the numpy array considering cyclic permutations.

    Parameters
    ----------
    arr1 : np.array consisting of only 0, 1, or -1. 


    Returns
    ----------
    longest_zero_sequence : Longest "circular" sequence of zeros in the np.array.

    """

    longest_zero_unrolled = np.array([])

    L = arr1.size

    for i in range(L):

        arr1_padded = np.concatenate((np.array([2]), np.roll(arr1, i), np.array([2]))) # Padded by dummy values

        # Finding the longest string of zeros in this rolled np.array
        nonzero_elements = np.where(arr1_padded !=0)[0] # Stores indices of non-zero elements
        string_zeros = np.diff(nonzero_elements) - 1 # Length of the strings of zeros
        longest_zero_unrolled = np.append(longest_zero_unrolled, np.max(string_zeros))

    longest_zero_rolled = np.max(longest_zero_unrolled)
    return longest_zero_rolled
