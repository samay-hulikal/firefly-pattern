import numpy as np

#WARN: Might be a good idea to consider how differing population sizes might influence the kinds of patterns that are evolved
#INFO: What really matters is not the absolute costs w_similarity and w_predation, but rather the ration between the quantities

def flash_pattern_evolution(n_flies_in_species, n_species, w_similarity, w_predation, L_seq, iterations):
    """
    Function that initializes flash patterns for all n_species * n_flies_in_species fireflies and also runs the pattern evolution algorithm on them.

    Parameters
    ----------
    n_species : Number of species of fireflies
    n_flies_in_species : Number of firefly agents per species
    w_similarity : Coefficient scaling the similarity cost
    w_predation : Coefficient scaling the predation risk
    L_seq : Length of the bit string that contains the flash pattern
    iterations : Number of cycles over which the evolution algorithm runs

    Returns
    ----------
    """

    all_patterns = np.random.randint(0, 2, (n_flies_in_species, n_species, L_seq)) # Assigns 0's and 1's (equal probability) such that pattern_matrix[i, j, :] is the flash pattern of firefly i of species j. Upper bound is exclusive in np.random.randint()
    costs = np.zeros((n_flies_in_species, n_species, iterations)) # costs[i, j, :] has the cost of firefly i of species j across all iterations of the algorithm
    buffer_size = 4
    #TODO: I am not sure why this buffer is necessary and why it cannot be defined more precisely from iterations
    similarity_scores = np.full((n_flies_in_species, n_species, buffer_size), np.nan) # Has to mostly be np.nan because a numerical value will affect the calculated average
    print(similarity_scores)



#INFO: Some test examples to check the function
flash_pattern_evolution(
        3,  # n_flies_in_species
        2,  # n_species
        1,  # w_similarity
        1,  # w_predation
        7,  # L_seq
        10  # iterations
        )

