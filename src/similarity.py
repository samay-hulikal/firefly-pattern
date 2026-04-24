import numpy as np

def longest_common_substring(p1, p2):
    """
    Checks the similarity between two binary strings of length L by mapping the bits to angles on a circle. These binary strings represent the flash patterns of two different SPECIES.

    Parameters
    ----------
    p1 : np.array
        One dimensional array containing binary values of length L specifying a flash pattern of an agent.

    p2 : np.array
        One dimensional array containing binary values of length L specifying a flash pattern of an agent.

    Returns
    ----------
    Returns the normalized similarity score s (number between 0 and 1).
    """

    # TODO: Do the two strings have to be from distinct SPECIES? Confirm the emphasis.
    angle_p1 = np.array([])
    angle_p2 = np.array([])

    # Transforming the strings to a list of angles that represent points on a circle
    if p1.size != p2.size:
        print("\nThe binary strings are not of the same size!!")
        return
    else:
        L = p1.size

        for i in range(L):
            if p1[i] != 0:
                angle_1 =  p1[i] * i * 2 * np.pi / L
                angle_p1 = np.append(angle_p1, angle_1)

            if p2[i] != 0:
                angle_2 =  p2[i] * i * 2 * np.pi / L
                angle_p2 = np.append(angle_p2, angle_2)
        
        # Tracking the similarity between angle_p2 and step-rotated versions of angle_p1
        # INFO: Rotated versions of angle_p1 are obtained by successively adding the array containing angles (in radians) with 2\pi/L. However, the angles need to be in [0, 2\pi).
        sim_scores = np.array([])

        for i in range(L):
            rotated_angle_p1 = angle_p1 + (2 * i * np.pi / L)  # Adding the discrete angle unit to effectively cause a cyclic rotation of the array
            rotated_angle_p1 = rotated_angle_p1 % (2 * np.pi) # Modulo 2\pi so that angles remain in [0, 2\pi).
            score = len([x for x in rotated_angle_p1 if np.any(np.isclose(x, angle_p2))])    # Calculates the intersection between the arrays and then calculates their length. Needs np.isclose(arr1, arr2, atol=1e-8, rtol=1e-5) (defaults) for floating points.
            sim_scores = np.append(sim_scores, score)

        return np.max(sim_scores)

a = np.array([1, 0, 1, 0, 0, 1])
b = np.array([1, 1, 1, 0, 0, 1])

print(longest_common_substring(a, b))
