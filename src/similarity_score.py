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
        common_substring = np.array([])

        for i in range(L):

            # Rotated version of p2
            p2_rotated = np.roll(p2, i) # Rolls the array right
            pdiff = p1 - p2_rotated

            # Finding the longest common "circular" substring between p1 and p2_rotated
            common_substring = np.append(common_substring, longest_zero_sequence_rolled(pdiff))
            #OPTIM: This method is leading to L^2 comparisons and slowing down the code; this is the main bottleneck. Use Chantal's method of doubling the sequence to compute similarity scores.

        return (np.max(common_substring)/L)

#INFO: Some test examples to check the function
# a = np.array([1, 0, 1, 0, 0, 0])
# b = np.array([1, 0, 1, 0, 0, 1])
# print(similarity_score(a, b))
