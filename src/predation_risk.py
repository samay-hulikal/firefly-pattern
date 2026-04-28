import numpy as np

def predation_risk(p):
    """
    Penalizes flashing straightforwardly-- counts the fraction of "ON" bits in the np.array. 

    Parameters
    ----------
    p : Binary np.array depicting the flash pattern of an agent.

    Returns
    ----------
    np.sum(p)/p.size : Total number of 1's over the length of the sequence.

    """
    return np.sum(p)/p.size

#INFO: Some test examples to check the function
# a = np.array([1, 0, 1, 0, 0, 0])
# print(predation_risk(a))

#WARN: Although this is an easy implementation, Chantal's code had a provision for including flash rapidity in the energy cost which she set to zero. Consider that as a potential source of energy cost as well. 
