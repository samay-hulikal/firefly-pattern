import numpy as np
from src.longest_zero_sequence import longest_zero_sequence_rolled

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
        print("\nThe two patterns have different lengths!")
        return
    else:
        
        L = p1.size
        common_substring = np.array([])

        for i in range(L):

            # Rotated version of p2
            p2_rotated = np.roll(p2, i) # Rolls the array right
            pdiff = p1 - p2_rotated

            # Finding the longest common "circular" substring between p1 and p2_rotated
            common_substring = np.append(common_substring, longest_zero_sequence_rolled(pdiff))
            print(p1)
            print(p2_rotated)
            print(common_substring)
            print("\n")

        return (np.max(common_substring)/L)

#INFO: Some test examples to check the function
# a = np.array([1, 0, 1, 0, 0, 0])
# b = np.array([1, 0, 1, 0, 0, 1])
# print(similarity_score(a, b))
