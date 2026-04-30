import numpy as np

#BUG: (Functional): This is a functional bug-- the problem is in the fundamental thought and not the implementation.
# Say firefly 1 and firefly 2 are compared and firefly 2 loses. Firefly 1's pattern is copied to firefly 2. Next, in the comparison between firefly 2 and firefly 3, firefly 2's NEW pattern (which happens to be firefly 1's) and firefly 3's original pattern are compared using similarity scores of firefly 2's ORIGINAL pattern.
# Now, if firefly 3 loses the similarity score battle, then firefly 2's NEW pattern (originally firefly 1's pattern) get scopied to firefly 3.
# The bug is just this absurdity.

def compete_all_and_copy(n_flies_in_species, n_species, allpatterns):
    """
    This is a reproduction of Chantal's MATLAB competition code without the memory bug. Every firefly competes with every other firefly and the winner is copied. However, 
    """
