import plotly.graph_objects as go
import numpy as np

def plot_species_costs(cost_array):
    """
    Plots the cost function: cost_array[i, j, t] = ((w_similarity * avg_sim_mat[i, j]) + (w_predation * predation_risk(all_patterns[i, j, :])))/(w_predation + w_similarity) averaged over every species j.

    Parameters
    ----------
    cost_array : cost_array[i, j, t] is the normalized evolutionary cost of firefly i of species j for generation/iteration t

    Returns
    ----------
    0 : Stores the plotted interactive html plots in figs/

    """
    print("Plotting the average costs...")   
    fig = go.Figure()

    # Extracting the number of species from cost_array
    arr_dims = cost_array.shape
    n_species = arr_dims[1]

    for j in range(n_species):
        avg_cost_of_species = np.mean(cost_array[:, j, :], axis=0) # Average cost across all fireflies in a given species
        fig.add_trace(go.Scatter(y=avg_cost_of_species, 
                                 name=f"Species {j}"))

    fig.update_layout(xaxis_title="Generation", yaxis_title="Average cost of each species")
    fig.write_html(f"figs/plots/avg_costs_{arr_dims[0]}_ffs_{arr_dims[1]}_sp_{arr_dims[2]}_gens.html") # Plots written to figs/
    
    print("Done plotting the average costs!")
    return 0
