import numpy as np
from scipy.stats import mode
from src.average_similarity_scores import average_similarity_scores

#WARN: Might be a good idea to consider how differing population sizes might influence the kinds of patterns that are evolved. For example, do simpler patterns emerge in species that are more populous?
#INFO: What really matters is not the absolute costs w_similarity and w_predation, but rather the ration between the quantities

def flash_pattern_evolution(n_flies_in_species, n_species, w_similarity, w_predation, L_seq, iterations):
    """
    Function that initializes flash patterns for all n_species * n_flies_in_species fireflies and also runs the pattern evolution algorithm on them.

    Parameters
    ----------
    n_flies_in_species : Number of firefly agents per species
    n_species : Number of species of fireflies
    w_similarity : Coefficient scaling the similarity cost
    w_predation : Coefficient scaling the predation risk
    L_seq : Length of the bit string that contains the flash pattern
    iterations : Number of cycles over which the evolution algorithm runs

    Returns
    ----------
    """

    all_patterns = np.random.randint(0, 2, (n_flies_in_species, n_species, L_seq)) # Assigns 0's and 1's (equal probability) such that pattern_matrix[i, j, :] is the flash pattern of firefly i of species j. Upper bound is exclusive in np.random.randint()
    costs = np.zeros((n_flies_in_species, n_species, iterations)) # costs[i, j, :] has the cost of firefly i of species j across all iterations of the algorithm
    #TODO: Do not fully understand costs
    buffer_size = 4
    #TODO: I am not sure why this buffer is necessary and why it cannot be defined more precisely from iterations
    similarity_scores = np.full((n_flies_in_species, n_species, buffer_size), np.nan) # Has to mostly be np.nan because a numerical value will affect the calculated average

    #INFO: Stored information starting at iteration t0 and in intervals of dt. The bit-wise mode of all fireflies in a given species is stored every dt iterations. Because the actual information stored is the bit-wise mode, early on, it's likely that no firefly actually has that pattern.
    t0 = 0
    dt = 2
    recording_indices = np.arange(t0, iterations + 1, dt) # Array of iterations when information needs to be recorded. Needs the + 1 because the upper bound is exclusive, again
    recorded_pattern_modes = np.zeros((n_species, L_seq, recording_indices.size)) # recorded_pattern_modes[j, :, t] is the bit-wise mode of all fireflies in species j at iteration t

    #INFO: Beginning of the evolution
    for t in range(iterations):
        # In this current generation...

        #INFO: Intra-species competition + mutations
        




    for j in range(n_species):
        recorded_pattern_modes[j, :, t0] = mode(all_patterns[:, j, :]).mode

    for j in range(n_species):
        print(f"Species {j}:\n")
        print(f"Mode of the species: {recorded_pattern_modes[j, :, t0]}")
        for i in range(n_flies_in_species):
            print(f"Pattern of firefly {i}: {all_patterns[i, j, :]}")



#INFO: Some test examples to check the function
flash_pattern_evolution(
        3,  # n_flies_in_species
        2,  # n_species
        1,  # w_similarity
        1,  # w_predation
        7,  # L_seq
        2  # iterations
        )

