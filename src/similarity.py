import numpy as np

def similarity(p1, p2):
    """
    Checks the similarity between two binary strings of length L using some complex number trickery. These binary strings represent the flash patterns of two different SPECIES.

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
    complex_p1 = []
    complex_p2 = []

    # Transforming the strings to a list of complex numbers that represent points on a circle
    if p1.size != p2.size:
        print("\nThe binary strings are not of the same size!!")
        return
    else:
        L = p1.size

        for i in range(L):
            if p1[i] != 0:
                cmplx_1 = np.exp(1j * p1[i] * i * 2 * np.pi / L)
                complex_p1.append(cmplx_1)

            if p2[i] != 0:
                cmplx_2 = np.exp(1j * p1[i] * i * 2 * np.pi / L)
                complex_p2.append(cmplx_2)


        return [complex_p1, complex_p2]

a = np.array([1, 0, 1, 0, 0, 1])
b = np.array([1, 1, 1, 0, 0, 1])

print(similarity(a, b))
