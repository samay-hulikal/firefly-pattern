import numpy as np
from src.mutations import flip_bit, swap_bit
from src.similarity_score import similarity_score
from src.predation_risk import predation_risk

#BUG: (Functional): This is a functional bug-- the problem is in the fundamental thought and not the implementation.
# Say firefly 1 and firefly 2 are compared and firefly 2 loses. Firefly 1's pattern is copied to firefly 2. Next, in the comparison between firefly 2 and firefly 3, firefly 2's NEW pattern (which happens to be firefly 1's) and firefly 3's original pattern are compared using similarity scores of firefly 2's ORIGINAL pattern.
# Now, if firefly 3 loses the similarity score battle, then firefly 2's NEW pattern (originally firefly 1's pattern) get copied to firefly 3.
# The bug is just this absurdity because what pattern propagates in this generation/iteration depends on which individual starts the comparisons.

def compete_all_and_copy(n_flies_in_species, n_species, w_similarity, w_predation, allpatterns, mutate_prob):
    """
    This is a reproduction of Chantal's MATLAB competition code without the memory bug. Every firefly competes with every other firefly and the winner is copied. Say firefly 1 and firefly 2 are compared and firefly 2 loses. Firefly 1's pattern is copied to firefly 2. Next, in the comparison between firefly 2 and firefly 3, firefly 2's NEW pattern (which happens to be firefly 1's) and firefly 3's original pattern are compared using similarity scores of firefly 2's ORIGINAL pattern. Now, if firefly 3 loses the similarity score battle, then firefly 2's NEW pattern (originally firefly 1's pattern) get copied to firefly 3. The bug is just this absurdity because what pattern propagates in this generation/iteration depends on which individual starts the comparisons (see #BUG above).

    Parameters
    ----------
    n_flies_in_species : Number of firefly agents per species
    n_species : Number of species of fireflies
    w_similarity : Coefficient scaling the similarity cost
    w_predation : Coefficient scaling the predation risk
    allpatterns : Contains flash patterns of all fireflies in all species-- allpatterns[i, j, :] is the flash pattern of firefly i belonging to species j
    mutate_prob : Used to determine mutation rate. np.random.rand() generates a random number in [0, 1]. Mutations are introduced if this number is less than mutate_prob.

    Returns
    ----------
    ptrns : np.array containing the results of mutations and copying

    """

    #INFO: Computing the average similarity scores
    avg_sim_mat = average_similarity_scores(n_flies_in_species, n_species, all_patterns) # Computing the average similarity scores between the fireflies in this generation/iteration


    #INFO: Intra-species competition + mutations
    ptrns = allpatterns.copy()

    for j in range(n_species):
        for i in range(n_flies_in_species):

            #INFO: Intra-species competition and pattern-copying

            for i2 in range(i + 1, n_flies_in_species):

                firefly1_pattern = ptrns[i, j, :]
                firefly2_pattern = ptrns[i2, j, :]

                #INFO: Calculating the total evolutionary costs for firefly1_pattern and firefly2_pattern
                score_firefly1 = (w_similarity * avg_sim_mat[i, j]) + (w_predation * predation_risk(firefly1_pattern))
                score_firefly2 = (w_similarity * avg_sim_mat[i2, j]) + (w_predation * predation_risk(firefly2_pattern))

                #INFO: Swap + mutate
                if score_firefly1 > score_firefly2: # If firefly1_pattern loses (has higher evolutionary cost), then firefly 1 takes on firefly 2's pattern
                    mutated_winner = firefly2_pattern.copy() # Copy of the winner's pattern (to be potentially mutated)

                    if np.random.rand() < mutate_prob: # mutate
                        if np.sum(mutated_winner) == 0 or np.sum(mutated_winner) == mutated_winner.size: # Patterns with all 0's or all 1's can mutate only by flipping
                            mutated_winner = flip_bit(mutated_winner)

                        else:
                            if np.random.randint(2) == 0:
                                mutated_winner = flip_bit(mutated_winner)
                            else:
                                mutated_winner = swap_bit(mutated_winner)

                    ptrns[i, j, :] = mutated_winner # The loser's pattern is replaced with the winner (+ possible mutations)

                elif score_firefly1 < score_firefly2: # If firefly1_pattern wins (has lower evolutionary cost), then firefly 2 takes on firefly 1's pattern
                    mutated_winner = firefly1_pattern.copy() # Copy of the winner's pattern (to be potentially mutated)

                    if np.random.rand() < mutate_prob: # mutate
                        if np.sum(mutated_winner) == 0 or np.sum(mutated_winner) == mutated_winner.size: # Patterns with all 0's or all 1's can mutate only by flipping
                            mutated_winner = flip_bit(mutated_winner)

                        else:
                            if np.random.randint(2) == 0:
                                mutated_winner = flip_bit(mutated_winner)
                            else:
                                mutated_winner = swap_bit(mutated_winner)

                    ptrns[i2, j, :] = mutated_winner # The loser's pattern is replaced with the winner (+ possible mutations)

                else: # If the scores of the two patterns are identical





