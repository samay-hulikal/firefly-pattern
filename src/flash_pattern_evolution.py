import numpy as np
from scipy.stats import mode
from src.compete_all_and_copy import compete_all_and_copy
from src.average_similarity_scores import average_similarity_scores
from src.predation_risk import predation_risk

#WARN: Might be a good idea to consider how differing population sizes might influence the kinds of patterns that are evolved. For example, do simpler patterns emerge in species that are more populous?
#INFO: What really matters is not the absolute costs w_similarity and w_predation, but rather the ration between the quantities

def flash_pattern_evolution(n_flies_in_species, n_species, w_similarity, w_predation, L_seq, iterations, mutation_probability):
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
    mutation_probability : Used to determine mutation rate. np.random.rand() generates a random number in [0, 1]. Mutations are introduced if this number is less than mutation_probability

    Returns
    ----------
    recorded_pattern_modes : Returns the bit-wise mode of all the fireflies in a given species- recorded_pattern_modes[j, :, t] is the bit-wise mode of species j for iteration/generation t
    recorded_costs : Returns the normalized evolutionary cost (similarity + predation risk)
    """

    all_patterns = np.random.randint(0, 2, (n_flies_in_species, n_species, L_seq)) # Assigns 0's and 1's (equal probability) such that pattern_matrix[i, j, :] is the flash pattern of firefly i of species j. Upper bound is exclusive in np.random.randint()

    #INFO: Stored information starting at iteration t0 and in intervals of dt. The bit-wise mode and evolutionary costs of all fireflies in a given species is stored every dt iterations. Because the actual pattern information stored is the bit-wise mode, early on, it's likely that no firefly actually has that pattern.
    recorded_pattern_modes = np.zeros((n_species, L_seq, iterations)) # recorded_pattern_modes[j, :, t] is the bit-wise mode of all fireflies in species j at iteration t
    recorded_costs = np.zeros((n_flies_in_species, n_species, iterations)) # recorded_costs[i, j, :] has the total evolutionary cost (predation risk and average similarity scores) of firefly i of species j across all iterations of the algorithm

    #INFO: Beginning of the evolution
    for t in range(iterations):
        # In this current generation...

        #INFO: Computing the average similarity scores
        avg_sim_mat = average_similarity_scores(n_flies_in_species, n_species, all_patterns) # Computing the average similarity scores between the fireflies in this generation/iteration

        #INFO: Recording the evolutionary costs BEFORE the patterns change
        for j in range(n_species):
            for i in range(n_flies_in_species):
                recorded_costs[i, j, t] = ((w_similarity * avg_sim_mat[i, j]) + (w_predation * predation_risk(all_patterns[i, j, :])))/(w_predation + w_similarity)

        #INFO: Intra-species competition + mutations
        all_patterns = compete_all_and_copy(n_flies_in_species, n_species, w_similarity, w_predation, all_patterns, avg_sim_mat, mutation_probability)

        #INFO: Recording the patterns AFTER mutation + copying
        for j in range(n_species):
            recorded_pattern_modes[j, :, t] = mode(all_patterns[:, j, :]).mode

    return recorded_pattern_modes, recorded_costs
