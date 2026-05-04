import numpy as np

def longest_zero_sequence_doubled(arr1):
    """
    Finds the longest sequence of zeros in the numpy array considering cyclic permutations.

    Parameters
    ----------
    arr1 : np.array consisting of only 0, 1, or -1. 


    Returns
    ----------
    longest_zero_sequence : Longest "circular" sequence of zeros in the np.array.

    """

    #INFO: Optimized search for the longest string of zeros by doubling the array
    arr1_doubled = np.concatenate([arr1, arr1])
    arr1_doubled_padded = np.concatenate((np.array([2]), arr1_doubled, np.array([2]))) # Padded by dummy values

    # Finding the longest string of zeros in this rolled np.array
    nonzero_elements = np.where(arr1_doubled_padded !=0)[0] # Stores indices of non-zero elements
    string_zeros = np.diff(nonzero_elements) - 1 # Length of the strings of zeros
    longest_zero_sequence = np.max(string_zeros)

    return min(longest_zero_sequence, arr1.size)

def similarity_score(p1, p2):
    """
    Computes the similarity between two patterns p1 and p2 and returns a score from 0 to 1. Similarity is defined as the longest "circular" substring that is present in p1 and cyclic permutations of p2. 

    Parameters
    ----------
    p1 : One dimensional np.array containing binary values of length L specifying a flash pattern of an agent.

    p2 : One dimensional np.array containing binary values of length L specifying a flash pattern of an agent.

    Returns
    ----------
    np.max(common_substring)/L : Returns the normalized similarity score s (between 0 and 1) defined as the longest "circular" substring in p1 and cyclic permutations of p2 divided by the length L of the string.
    """
    
    if p1.size != p2.size:
        raise ValueError("The two patterns have different lengths!")
    else:
        
        L = p1.size
        longest_zero = 0

        for i in range(L):

            # Rotated version of p2
            p2_rotated = np.roll(p2, i) # Rolls the array right
            pdiff = p1 - p2_rotated

            # Finding the longest common "circular" substring between p1 and p2_rotated
            run = longest_zero_sequence_doubled(pdiff)
            if run > longest_zero:
                longest_zero = run

        return longest_zero/L

#INFO: Some test examples to check the function
# a = np.array([0, 0, 1, 0, 0, 0])
# b = np.array([1, 0, 1, 0, 0, 1])
# print(longest_zero_sequence_doubled(a))
# print(similarity_score(a, b))
