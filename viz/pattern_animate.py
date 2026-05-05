import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

def roll_start_one(ptn):
    """
    Rolls a pattern so that the visualized pattern always begin with a 1.

    Parameters
    ----------
    ptn : Pattern that needs to be plotted

    Returns
    ----------
    rolled_ptn : Left-rolled pattern until the closest 1 is brought to the first bit
    """

    ones_position = np.where(ptn == 1)[0] # Position of the 1's
    if ones_position.size == 0: # If all the bits are zero
        print("The mode of this species has all bits being 0's!")
        return ptn # Returns the same array if all bits are zero

    return np.roll(ptn, -ones_position[0]) # Left-rolling the 


def evolution_movie(recorded_modes, mutprob, fps=10, stride=1):
    """
    Animate the evolution of the pattern modes over time.

    Parameters
    ----------
    recorded_modes : recorded_modes[j, :, t] is the bit-wise mode of all fireflies in species j at iteration t
    mutprob : Mutation probability; used only to name the animations
    fps : Frames per second for the movie
    stride : Frames every stride generations

    Returns
    ----------
    0 : Saves the animation to figs/ as an .mp4 file
    """

    n_species, L_seq, n_gens = recorded_modes.shape
    frame_indices = range(0, n_gens, stride)

    cmap = ListedColormap(["white", "yellow"]) # Colormap: 0-> white, 1-> yellow
    fig, ax = plt.subplots(figsize=(10, n_species))

    print("Generating movie...")
    
    def update(frame_num): # Function that updates the "subplots" for each species
        t = frame_num * stride
        ax.clear()

        frame = np.zeros((n_species, L_seq))
        for j in range(n_species):
            mde = recorded_modes[j, :, t]
            frame[j, :] = roll_start_one(mde)
        
        ax.imshow(frame, cmap=cmap, aspect="auto", vmin=0, vmax=1)

        # Labels and ticks
        ax.set_yticks(range(n_species))
        ax.set_yticklabels([f"Species {j}" for j in range(n_species)])
        ax.set_xlabel("Bit position")
        ax.set_title(f"Generation {t}")
        ax.set_xticks(np.arange(-0.5, L_seq, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, n_species, 1), minor=True)

        # Adding grid lines to separate each bit
        ax.grid(which="minor", color="gray", linewidth=0.5)
        ax.tick_params(which="minor", size=0)
    
    ani = animation.FuncAnimation(fig, # Figure to animate
                                  update, # Function to draw each frame
                                  frames=len(frame_indices), # Number of times to call update
                                  interval=1000//fps # Interval between frames rounded to the nearest integer
                                  )
    ani.save(f"figs/animations/{n_species}_species_at_{fps}_fps_{n_gens}_generations_{mutprob}_mutprob.mp4", fps=fps)
    plt.close()
    print(f"Movie saved!")
