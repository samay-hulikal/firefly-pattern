from src.flash_pattern_evolution import flash_pattern_evolution
from viz.species_costs import plot_species_costs
from viz.pattern_animate import evolution_movie

n_fireflies = 100
n_species = 10
w_similarity = 3
w_predation = 1
seq_length = 75
iters = 2000
mutate_prob = 0.4

#INFO: Costs are recorded for EVERY iteration while the patterns are recorded every dt iterations. 
# To change the rate of data recording, you'll need to modify the variable dt in the function flash_pattern_evolution() in src.flash_pattern_evolution
rec_ps, rec_cts = flash_pattern_evolution(
            n_fireflies,  # n_flies_in_species
            n_species,  # n_species
            w_similarity,  # w_similarity
            w_predation,  # w_predation
            seq_length,  # L_seq
            iters,  # iterations
            mutate_prob # mutation_probability
            )


plot_species_costs(rec_cts)
# print(rec_ps[3, :, -1])
evolution_movie(rec_ps, mutate_prob)
# print(rec_ps)
# print(rec_cts)
# for j in range(n_species):
#     recorded_pattern_modes[j, :, t0] = mode(all_patterns[:, j, :]).mode
#
# for j in range(n_species):
#     print(f"Species {j}:\n")
#     print(f"Mode of the species: {recorded_pattern_modes[j, :, t0]}")
#     for i in range(n_flies_in_species):
#         print(f"Pattern of firefly {i}: {all_patterns[i, j, :]}")
