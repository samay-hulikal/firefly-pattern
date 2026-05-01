import numpy as np
from src.similarity_score import similarity_score

def average_similarity_scores(n_flies_in_species, n_species, allpatterns):
    """
    Given all the patterns of all species where allpatterns[i, j, :] is the flash pattern of firefly i belonging to species j, this function returns a matrix with all the average similarity scores.

    Parameters
    ----------
    n_flies_in_species : Number of firefly agents per species
    n_species : Number of species of fireflies
    allpatterns : Contains flash patterns of all fireflies in all species-- allpatterns[i, j, :] is the flash pattern of firefly i belonging to species j

    Returns
    ----------
    average_similarity_score_matrix : Contains the average similarity score of every fly in comparison to all flies of every other species-- average_similarity_score_matrix[i, j] is the averaged similarity score of fly i in species j
    """

    average_similarity_score_matrix = np.zeros((n_flies_in_species, n_species))

    #OPTIM: Claude thinks that this might also be a speed bottleneck and using vector operations might negate the for loops
    for j in range(n_species):
        for i in range(n_flies_in_species):
            #INFO: Computing the average similarity score of a given firefly

            sim_score_ij = np.array([]) # Records all similarity scores of firefly i in species j
            for j1 in range(n_species):
                for i1 in range(n_flies_in_species):
                    if j1 == j: # Do not compare the pattern of fireflies in the same species
                        continue
                    else:
                        sim_score_ij = np.append(sim_score_ij, similarity_score(allpatterns[i, j, :], allpatterns[i1, j1, :]))


            average_similarity_score_matrix[i, j] = np.mean(sim_score_ij) # The average of all these scores is added to the matrix

    return average_similarity_score_matrix
