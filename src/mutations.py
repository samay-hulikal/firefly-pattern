import numpy as np

def flip_bit(p):
    """
    Selects a random location in the flash pattern and flips the bit. This moves the evolution algorithm in the direction of total flash number gradients.

    Parameters
    ----------
    p : Binary np.array representing the flash pattern.

    Returns
    ----------
    p_flipped_bit : Binary sequence with one flipped bit.
    """
    
    p_flipped_bit = p.copy() # Numpy arrays are passed as references and I do not want to work on the original array unintentionally

    rand_location = np.random.randint(0, p.size) # The upper bound is exclusive-- integers are generated from [0 to p.size -1]
    p_flipped_bit[rand_location] = 1 - p_flipped_bit[rand_location]
    return p_flipped_bit


def swap_bit(p):
    """
    Selects a random location in the flash pattern and swaps the bit with the neighbor to its right. This moves the evolution algorithm in the direction of constant total flash number.

    Parameters
    ----------
    p : Binary np.array representing the flash pattern.

    Returns
    ----------
    p_swapped_right : Binary sequence with one right-swapped bit.
    """

    p_swapped_right = p.copy() # Numpy arrays are passed as references and I do not want to work on the original array unintentionally

    rand_location = np.random.randint(0, p.size) # The upper bound is exclusive-- integers are generated from [0 to p.size -1]
    rand_location_right = (rand_location + 1) % p.size # Ensures that the last element can swap with the first element
    #WARN: The above is a slight change from Chantal's code where the end cannot swap with the first element.
    
    p_swapped_right[rand_location], p_swapped_right[rand_location_right] =  p_swapped_right[rand_location_right], p_swapped_right[rand_location] # You need to perform this assignment simultaneously so as not to rewrite the np.array.
    return p_swapped_right

#INFO: Some test examples to check the function
# a = np.array([1, 0, 1, 0, 0, 0])
# print(flip_bit(a))
# print(swap_bit(a))
